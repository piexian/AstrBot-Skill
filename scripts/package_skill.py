from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


DEFAULT_SKILL_NAME = "skill-astrbot-dev"
DEFAULT_SOURCE_DIR = Path("docs")
DEFAULT_OUTPUT_DIR = Path("dist")

EXCLUDED_DIRS = {
    ".tmp",
    "__pycache__",
    "node_modules",
    "venv",
}
EXCLUDED_FILES = {
    ".DS_Store",
}
EXCLUDED_SUFFIXES = {
    ".pyc",
}


def should_include(path: Path, source_dir: Path) -> bool:
    relative = path.relative_to(source_dir)
    if any(part in EXCLUDED_DIRS for part in relative.parts):
        return False
    if path.name in EXCLUDED_FILES:
        return False
    return path.suffix not in EXCLUDED_SUFFIXES


def iter_skill_files(source_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in source_dir.rglob("*")
        if path.is_file() and should_include(path, source_dir)
    )


def resolve_entrypoint(source_dir: Path) -> Path:
    entrypoint = source_dir / "SKILL.md"
    if entrypoint.is_file():
        return entrypoint
    raise FileNotFoundError(f"Missing skill entrypoint: {entrypoint}")


def build_skill_zip(source_dir: Path, output_path: Path, skill_name: str) -> Path:
    source_dir = source_dir.resolve()
    output_path = output_path.resolve()

    if not source_dir.is_dir():
        raise FileNotFoundError(f"Skill source directory not found: {source_dir}")

    resolve_entrypoint(source_dir)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    files = iter_skill_files(source_dir)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            arcname = Path(skill_name) / path.relative_to(source_dir)
            archive.write(path, arcname.as_posix())

    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package docs/ as an installable AstrBot/Codex Skill zip."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Skill source directory. Defaults to docs/.",
    )
    parser.add_argument(
        "--name",
        default=DEFAULT_SKILL_NAME,
        help=f"Top-level folder name inside the zip. Defaults to {DEFAULT_SKILL_NAME}.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_DIR / f"{DEFAULT_SKILL_NAME}.zip",
        help="Output zip path. Defaults to dist/skill-astrbot-dev.zip.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output_path = build_skill_zip(args.source, args.output, args.name)
    except Exception as exc:
        print(f"Failed to package skill: {exc}", file=sys.stderr)
        return 1

    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
