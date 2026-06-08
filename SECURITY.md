# Security Policy

This repository must not contain secrets, credentials, private prompts, runtime dumps, logs, real backups, or machine-specific configuration.

Before publishing, run:

```bash
cd geo-control-plane
python scripts/validate_yaml.py
```

Use GitHub secret scanning and push protection for public repositories.

