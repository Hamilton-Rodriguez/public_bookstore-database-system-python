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