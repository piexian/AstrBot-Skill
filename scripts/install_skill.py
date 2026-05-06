from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from package_skill import (
    DEFAULT_SKILL_NAME,
    DEFAULT_SOURCE_DIR,
    resolve_entrypoint,
    should_include,
)


def default_skills_root() -> Path:
    return Path.home() / ".codex" / "skills"


def copy_skill(source_dir: Path, target_dir: Path, force: bool) -> Path:
    source_dir = source_dir.resolve()
    target_dir = target_dir.expanduser().resolve()

    if not source_dir.is_dir():
        raise FileNotFoundError(f"Skill source directory not found: {source_dir}")

    resolve_entrypoint(source_dir)

    if target_dir.exists():
        if not force:
            raise FileExistsError(
                f"{target_dir} already exists. Re-run with --force to replace it."
            )
        shutil.rmtree(target_dir)

    def ignore(directory: str, names: list[str]) -> set[str]:
        directory_path = Path(directory)
        ignored = set()
        for name in names:
            path = directory_path / name
            if not should_include(path, source_dir):
                ignored.add(name)
        return ignored

    target_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, target_dir, ignore=ignore)
    return target_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install docs/ as a local Codex/Agent skill."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Skill source directory. Defaults to docs/.",
    )
    parser.add_argument(
        "--skills-root",
        type=Path,
        default=default_skills_root(),
        help="Directory that contains local skills. Defaults to ~/.codex/skills.",
    )
    parser.add_argument(
        "--name",
        default=DEFAULT_SKILL_NAME,
        help=f"Installed skill directory name. Defaults to {DEFAULT_SKILL_NAME}.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed copy.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_dir = args.skills_root / args.name

    try:
        installed_dir = copy_skill(args.source, target_dir, args.force)
    except Exception as exc:
        print(f"Failed to install skill: {exc}", file=sys.stderr)
        return 1

    print(f"Installed {args.name} to {installed_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
