import oci
import base64

# Load the configuration from the config file
config = oci.config.from_file("/home/opc/.oci/config")

# Initialize the IdentityClient
identity = oci.identity.IdentityClient(config)
compartments = identity.list_compartments(config["tenancy"]).data

# Print compartment names and IDs
for compartment in compartments:
    print(compartment.name, compartment.id)



# Initialize the SecretsClient
secrets_client = oci.secrets.SecretsClient(config)

# Specify the OCID of the secret you want to retrieve
secret_id = "ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaa7cw476u7eebw62gya4k6kgc4soirh46hngleak3dnsma"

# Retrieve the secret
response = secrets_client.get_secret_bundle(secret_id)
secret_value = response.data.secret_bundle_content.content

# Decode the base64 encoded secret value
decoded_secret_value = base64.b64decode(secret_value).decode('utf-8')
print("Secret Value:", decoded_secret_value)

# region=us-ashburn-1
# region=sa-bogota-1

# Backup Config file:
#[DEFAULT]
#user=ocid1.user.oc1..aaaaaaaakfh3sxydhvfa5hamgfo7xw2pqpa4nb636ymobq3ougamz2zdz7za
#fingerprint=e6:35:37:81:1b:4f:59:e4:9a:7c:ef:97:36:45:4f:fb
#key_file=/home/opc/.ssh/45111301@claro.com.co_2024-09-19T15_15_23.618Z.pem
#tenancy=ocid1.tenancy.oc1..aaaaaaaawttxo6zmedll5b35bsjcvdx5bmobygwx7avyofsxxawvwaps26xq
#region=sa-bogota-1

# En el archivo del webserver Backup archivo Config
# echo "W0RFRkFVTFRdDQp1c2VyPW9jaWQxLnVzZXIub2MxLi5hYWFhYWFhYWtmaDNzeHlkaHZmYTVoYW1nZm83eHcycHFwYTRuYjYzNnltb2JxM291Z2FtejJ6ZHo3emENCmZpbmdlcnByaW50PWU2OjM1OjM3OjgxOjFiOjRmOjU5OmU0OjlhOjdjOmVmOjk3OjM2OjQ1OjRmOmZiDQprZXlfZmlsZT0vaG9tZS9vcGMvLnNzaC80NTExMTMwMUBjbGFyby5jb20uY29fMjAyNC0wOS0xOVQxNV8xNV8yMy42MThaLnBlbQ0KdGVuYW5jeT1vY2lkMS50ZW5hbmN5Lm9jMS4uYWFhYWFhYWF3dHR4bzZ6bWVkbGw1YjM1YnNqY3ZkeDVibW9ieWd3eDdhdnlvZnN4eGF3dndhcHMyNnhxDQpyZWdpb249dXMtYXNoYnVybi0x" | base64 --decode > /home/opc/.oci/config

