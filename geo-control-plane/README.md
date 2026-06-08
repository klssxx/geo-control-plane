🌐 **Language:** [English](README.md) · [Español](README.es.md)

# GEO Control Plane

A safety-first control layer for AI coding agents.

## What Problem Does It Solve?

AI agents often mix planning, execution, and validation in a single step. GEO Control Plane separates them into explicit routes and requires gates before risky actions.

## Core Routes

| route | purpose |
| --- | --- |
| `AUDIT` | inspect without writing |
| `PLAN` | propose changes without executing |
| `DOCS` | create or clean documentation after authorization |
| `CODE` | modify workspace files after authorization |
| `VALIDATE` | verify real results |
| `DIVERGE` | generate unusual options without accepting them |
| `RED_REVIEW` | challenge unsafe or incomplete proposals |

## Start Here

1. Read `QUICKSTART.md`.
2. Run the AUDIT example.
3. Review `docs/GATES.md`.
4. Validate the YAML manifest:

```bash
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

## Agents And Models

| agent/model | good use | boundary |
| --- | --- | --- |
| `Human Owner` | final approval and priority | must provide explicit gates |
| `GEO Control Plane` | scope, routing, risk, rollback, validation | does not execute by itself |
| `Codex` | code edits, file validation, repository work | bounded by routes and gates |
| `Hermes Agent` | future orchestration pattern | not enabled in this public template |
| high-reasoning LLM | architecture review, critique, divergence | recommendations only without gates |

## What You Can Do With It

- Audit a repository before allowing writes.
- Separate planning from execution.
- Require rollback before material changes.
- Validate YAML control files.
- Document high-risk requests as `RED_REVIEW`.
- Keep creative suggestions in `DIVERGE` until critique and validation.

## What This Template Does Not Do

- It does not install packages.
- It does not start services.
- It does not dispatch workers.
- It does not provide credentials.
- It does not grant access to your filesystem.

## Architecture

```text
HUMAN OWNER
└── GEO CONTROL PLANE
    ├── policy: GEO-MANIFEST.yaml
    ├── index: MASTER_INDEX.md
    ├── docs: docs/*.md
    ├── examples: examples/*.md
    └── validation: scripts/validate_yaml.py
```
