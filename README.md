# GEO Control Plane Public Edition

A safety-first orchestration template for AI coding agents.

## What Problem Does It Solve?

AI agents often mix planning, execution, and validation in a single step. GEO Control Plane separates them into explicit routes and requires gates before risky actions.

## Core Routes

- `AUDIT` - inspect without writing
- `PLAN` - propose changes without executing
- `CODE` - modify workspace files after authorization
- `VALIDATE` - verify real results
- `DIVERGE` - generate unusual options without accepting them
- `RED_REVIEW` - challenge unsafe or incomplete proposals

## Start Here

1. Read [QUICKSTART.md](geo-control-plane/QUICKSTART.md).
2. Run the [AUDIT example](geo-control-plane/examples/audit-only-example.md).
3. Review the [gate model](geo-control-plane/docs/GATES.md).
4. Validate the YAML manifest:

```bash
cd geo-control-plane
python scripts/validate_yaml.py
```

Expected output:

```text
YAML_PARSE_PASS 2
MANIFEST_INDEX_PASS
README_REGISTRATION_PASS
FILES_CHECKED 24
RESULT PASS
```

## Public Safety Position

This public edition is documentation and validation only. It does not include runtime dumps, credentials, backups, private prompts, package logs, API keys, or machine-specific configuration.

## Repository Layout

```text
geo-control-plane/
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── GEO-MANIFEST.yaml
├── MASTER_INDEX.md
├── QUICKSTART.md
├── docs/
├── examples/
└── scripts/
```

Repository-level files are also included: `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.gitignore`, and `.github/workflows/validate.yml`.
