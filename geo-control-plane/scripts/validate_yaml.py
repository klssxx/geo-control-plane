#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = ROOT.parent

YAML_FILES = [
    ROOT / "GEO-MANIFEST.yaml",
    REPOSITORY_ROOT / ".github/workflows/validate.yml",
]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "GEO-MANIFEST.yaml",
    "MASTER_INDEX.md",
    "QUICKSTART.md",
    "docs/ARCHITECTURE.md",
    "docs/WORKFLOWS.md",
    "docs/GATES.md",
    "docs/RUNTIME_LIMITS.md",
    "examples/audit-only-example.md",
    "examples/safe-code-change-example.md",
    "examples/red-review-example.md",
    "examples/diverge-example.md",
    "examples/validate-yaml-example.md",
    "scripts/validate_yaml.py",
]

REPOSITORY_FILES = [
    "../README.md",
    "../LICENSE",
    "../SECURITY.md",
    "../CONTRIBUTING.md",
    "../CODE_OF_CONDUCT.md",
    "../.gitignore",
    "../.github/workflows/validate.yml",
]


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    for path in YAML_FILES:
        load_yaml(path)

    manifest = load_yaml(ROOT / "GEO-MANIFEST.yaml")
    canonical_files = manifest.get("canonical_files", [])
    repository_files = manifest.get("repository_files", [])

    missing = [file for file in REQUIRED_FILES if not (ROOT / file).exists()]
    missing += [file for file in REPOSITORY_FILES if not (ROOT / file).exists()]
    if missing:
        print("FILES_MISSING " + ",".join(missing))
        return 1

    unregistered = [file for file in REQUIRED_FILES if file not in canonical_files]
    unregistered += [file for file in REPOSITORY_FILES if file not in repository_files]
    if unregistered:
        print("MANIFEST_INDEX_FAIL " + ",".join(unregistered))
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "GEO Control Plane" not in readme or "Core Routes" not in readme:
        print("README_REGISTRATION_FAIL")
        return 1

    print(f"YAML_PARSE_PASS {len(YAML_FILES)}")
    print("MANIFEST_INDEX_PASS")
    print("README_REGISTRATION_PASS")
    print("FILES_CHECKED 24")
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
