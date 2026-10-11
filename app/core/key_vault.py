from functools import lru_cache
import os

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


@lru_cache
def _client() -> SecretClient | None:
    vault_uri = os.environ.get("AZURE_KEY_VAULT_URI")
    if not vault_uri:
        return None
    credential = ClientSecretCredential(
        tenant_id=os.environ["AZURE_TENANT_ID"],
        client_id=os.environ["AZURE_CLIENT_ID"],
        client_secret=os.environ["AZURE_CLIENT_SECRET"],
    )
    return SecretClient(vault_url=vault_uri, credential=credential)


def get_secret(name: str) -> str | None:
    """Returns the named Key Vault secret, or None if no vault is configured for this workspace."""
    client = _client()
    if client is None:
        return None
    return client.get_secret(name).value
