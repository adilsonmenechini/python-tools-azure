#
#  Copy secret KeyVault to different KeyVault
#

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Informações do Key Vault de origem
source_vault_name = "sandbox-handson-kv-001"
source_vault_url = f"https://sandbox-handson-kv-001.vault.azure.net/"

# Informações do Key Vault de destino
destination_vault_name = "sandbox-handson-002"
destination_vault_url = f"https://sandbox-handson-kv-002.vault.azure.net/"

# Criação do cliente para o Key Vault de origem
source_credential = DefaultAzureCredential()
source_secret_client = SecretClient(vault_url=source_vault_url, credential=source_credential)

# Criação do cliente para o Key Vault de destino
destination_credential = DefaultAzureCredential()
destination_secret_client = SecretClient(vault_url=destination_vault_url, credential=destination_credential)

# Listar todas as chaves secretas do Key Vault de origem
secrets = source_secret_client.list_properties_of_secrets()

for secret in secrets:
    # Obter cada chave secreta do Key Vault de origem
    secret_name = secret.name
    retrieved_secret = source_secret_client.get_secret(secret_name)

    # Criar a mesma chave secreta no Key Vault de destino
    destination_secret_client.set_secret(secret_name, retrieved_secret.value)

    print(f"Chave secreta '{secret_name}' migrada com sucesso.")

print("Migração de chaves secretas concluída.")
