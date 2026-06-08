# Security Policy

## Scope

This repository is a documentation and validation template. It should not contain secrets, credentials, runtime dumps, private prompts, private backups, or machine-specific configuration.

## Before Publishing

Run a secret audit before the first public push. At minimum, inspect for:

- API keys
- tokens
- passwords
- private file paths that reveal sensitive data
- runtime dumps
- logs
- credentials

GitHub secret scanning and push protection are recommended for public repositories.

## Reporting Issues

Open a GitHub issue for documentation mistakes, unsafe examples, missing rollback guidance, or accidental sensitive content.

