# QUICKSTART

## 1. Clone Or Open The Repository

```bash
cd geo-control-plane
```

## 2. Read The Public Boundary

Start with:

- `README.md`
- `docs/GATES.md`
- `docs/RUNTIME_LIMITS.md`

## 3. Run Validation

```bash
python scripts/validate_yaml.py
```

Expected:

```text
YAML_PARSE_PASS 2
MANIFEST_INDEX_PASS
README_REGISTRATION_PASS
FILES_CHECKED 24
RESULT PASS
```

## 4. Try The Examples

- `examples/audit-only-example.md`
- `examples/safe-code-change-example.md`
- `examples/red-review-example.md`

## 5. Adapt Safely

When adapting this template:

- keep private paths out of public files
- keep gates literal
- keep validation reproducible
- do not mix planning and execution
