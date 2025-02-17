import oci
import base64

def get_config(region):
    return oci.config.from_file(profile_name=region)

### Using sa-bogota-1 region
config_sa_bogota = get_config("sa-bogota-1")
secrets_client = oci.secrets.SecretsClient(config_sa_bogota)


# Specify the OCID of the secrets you want to retrieve

vault_secrets = [
    "ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaagc67tpnxo3yb7g5wplsiycihsabjmc56g7cwnk2zgy5a",     # secret_id_user
    "ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaagctdfqix6ohnctyc4tuz6qegrrk5bcqnsdv5lqxvubmq",     # secret_id_password
    "ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaadbqyfmh763jgl33tpbvkbodsso6vtfmpcagjtjoqdusq",     # secret_id_database
    "ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaa7cw476u7eebw62gya4k6kgc4soirh46hngleak3dnsma"    # secret_id_host
]

# Retrieve the secrets

for secret_id in vault_secrets:
    rsponse = secrets_client.get_secret_bundle(secret_id)
    secret_value = response.data.secret_bundle_content.content

    # Decode the base64 encoded secret value
    decoded_secret_value = base64.b64decode(secret_value).decode('utf-8')
    print("Secret Value:", decoded_secret_value)





