#
#  Key Vault reference App Configuration
#

import azure.identity, json
from azure.keyvault.secrets import SecretClient
from azure.appconfiguration import AzureAppConfigurationClient
from azure.appconfiguration._models import ConfigurationSetting

# Defina suas informações de autenticação
credential = azure.identity.DefaultAzureCredential()

# Defina as informações do Key Vault
keyvault_name = 'https://sandbox-handson-002'
keyvault_uri = f"https://sandbox-handson-kv-002.vault.azure.net/"

# Defina as informações do App Configuration
appconfig_connection_string = 'Endpoint=https://sandbox-handson-appconfig-002.azconfig.io;Id=61Ag;Secret=Wm5v-GIT-0O0O0-EXEMPLO-0O0-SECRET-AJp8k='

try:
    # Crie instâncias dos clientes do Azure Key Vault e do Azure App Configuration
    keyvault_client = SecretClient(vault_url=keyvault_uri, credential=credential)
    appconfig_client = AzureAppConfigurationClient.from_connection_string(appconfig_connection_string)

    # Liste todas as secrets do Azure Key Vault
    secrets = keyvault_client.list_properties_of_secrets()

    # Crie as referências do Key Vault no Azure App Configuration
    for secret in secrets:
        secret_name = secret.name
        secret_value = keyvault_client.get_secret(secret_name).value

        print(secret_name)

        # Crie a referência do Key Vault no Azure App Configuration como um objeto ConfigurationSetting
        keyvault_reference = ConfigurationSetting(
            key=secret_name,
            value=json.dumps({
                "uri": keyvault_uri,
                "secretName": secret_name,
            }),
            content_type="application/vnd.microsoft.appconfig.keyvaultref+json;charset=utf-8"
        )

        # Defina a referência do Key Vault no Azure App Configuration
        appconfig_client.set_configuration_setting(keyvault_reference)

    print("Referências do Key Vault criadas com sucesso no Azure App Configuration!")

except Exception as e:
    print(f"Ocorreu um erro durante a criação das referências: {str(e)}")