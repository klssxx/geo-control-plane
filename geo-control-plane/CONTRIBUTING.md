🌐 **Language:** [English](CONTRIBUTING.md) · [Español](CONTRIBUTING.es.md)

# Contributing

Contributions should preserve the control-plane boundaries.

## Rules

- Keep planning, execution, validation, and recovery separate.
- Do not add runtime activation examples without explicit gates.
- Do not add secrets, tokens, private prompts, logs, or real backups.
- Keep examples reproducible and anonymized.
- Update `GEO-MANIFEST.yaml` and `MASTER_INDEX.md` when adding public files.
- Run `python scripts/validate_yaml.py` before opening a pull request.

## Good Contributions

- clearer workflows
- safer gates
- better validation checks
- anonymized examples
- documentation that reduces ambiguity

