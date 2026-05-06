from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "scripts"))

from install_skill import copy_skill  # noqa: E402
from package_skill import build_skill_zip  # noqa: E402


class SkillPackagingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="astrbot-skill-test-"))
        self.source_dir = self.tmpdir / "docs"
        self.source_dir.mkdir()
        (self.source_dir / "SKILL.md").write_text("# skill\n", encoding="utf-8")
        (self.source_dir / "index.md").write_text("# index\n", encoding="utf-8")
        (self.source_dir / "agent").mkdir()
        (self.source_dir / "agent" / "runner.md").write_text("runner\n", encoding="utf-8")
        (self.source_dir / ".tmp").mkdir()
        (self.source_dir / ".tmp" / "scratch.md").write_text("scratch\n", encoding="utf-8")
        (self.source_dir / "__pycache__").mkdir()
        (self.source_dir / "__pycache__" / "cache.pyc").write_bytes(b"cache")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_build_skill_zip_uses_installable_top_level_folder(self) -> None:
        output_path = self.tmpdir / "skill.zip"

        build_skill_zip(self.source_dir, output_path, "skill-astrbot-dev")

        with zipfile.ZipFile(output_path) as archive:
            names = set(archive.namelist())

        self.assertIn("skill-astrbot-dev/SKILL.md", names)
        self.assertIn("skill-astrbot-dev/index.md", names)
        self.assertIn("skill-astrbot-dev/agent/runner.md", names)
        self.assertNotIn("skill-astrbot-dev/.tmp/scratch.md", names)
        self.assertNotIn("skill-astrbot-dev/__pycache__/cache.pyc", names)

    def test_copy_skill_installs_and_requires_force_for_replace(self) -> None:
        target_dir = self.tmpdir / "skills" / "skill-astrbot-dev"

        installed_dir = copy_skill(self.source_dir, target_dir, force=False)

        self.assertEqual(target_dir, installed_dir)
        self.assertTrue((target_dir / "SKILL.md").is_file())
        self.assertFalse((target_dir / ".tmp" / "scratch.md").exists())

        with self.assertRaises(FileExistsError):
            copy_skill(self.source_dir, target_dir, force=False)

        (self.source_dir / "index.md").write_text("# updated\n", encoding="utf-8")
        copy_skill(self.source_dir, target_dir, force=True)
        self.assertEqual("# updated\n", (target_dir / "index.md").read_text(encoding="utf-8"))

    def test_repository_docs_package_contains_runtime_entrypoints(self) -> None:
        output_path = self.tmpdir / "skill.zip"

        build_skill_zip(ROOT_DIR / "docs", output_path, "skill-astrbot-dev")

        with zipfile.ZipFile(output_path) as archive:
            names = set(archive.namelist())

        self.assertIn("skill-astrbot-dev/SKILL.md", names)
        self.assertIn("skill-astrbot-dev/index.md", names)
        self.assertIn("skill-astrbot-dev/plugin_config/hooks.md", names)
        self.assertNotIn("skill-astrbot-dev/.tmp/hook_inventory/index.md", names)

    def test_repository_contains_only_installable_docs_skill_entrypoint(self) -> None:
        skill_files = [
            path.relative_to(ROOT_DIR).as_posix()
            for path in ROOT_DIR.rglob("SKILL.md")
            if ".git" not in path.parts
        ]

        self.assertEqual(["docs/SKILL.md"], skill_files)


if __name__ == "__main__":
    unittest.main()
