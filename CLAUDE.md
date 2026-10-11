# Instructions for AI coding agents

- Never hardcode a secret, API key, token, or connection string in code. Never paste a literal value as a "temporary" placeholder either, even one meant to be replaced later.
- This project's available Key Vault secrets are listed at the start of every conversation (a system note naming each key and a one-line description). Fetch a value with:
  ```python
  from app.core.key_vault import get_secret
  value = get_secret("<key-name>")
  ```
  Use the exact key name given in that note.
- If the secret you need isn't in that list, stop and tell the user to add it via the Studio's "Secrets" panel. Suggest a kebab-case key name (e.g. `stripe-api-key`) and a short description, rather than inventing a value or writing a TODO with a fake one.
- The app still runs fine on `.env` defaults (SQLite, a generated `SECRET_KEY`) when no Key Vault is configured at all. That's the normal local/offline path and nothing about it changes.
- `database_url` and `secret_key` are already wired vault-first in `app/core/config.py`'s `get_settings()`. Anything else (a third-party API key used inside one route) can just call `get_secret(name)` directly at the point of use. It doesn't need a `Settings` field.
