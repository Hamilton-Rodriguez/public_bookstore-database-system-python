from flask import Flask, render_template
import mysql.connector
import oci
import base64

app = Flask(__name__)

def get_config(region):
    return oci.config.from_file(profile_name=region)

### Using sa-bogota-1 region
config_sa_bogota = get_config("sa-bogota-1")
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# Initialize the SecretsClient
secrets_client = oci.secrets.SecretsClient(config_sa_bogota)

# Retrieve the vault secrets contents

vault_user = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaagc67tpnxo3yb7g5wplsiycihsabjmc56g7cwnk2zgy5a'
vault_password = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaagctdfqix6ohnctyc4tuz6qegrrk5bcqnsdv5lqxvubmq'
vault_database = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaadbqyfmh763jgl33tpbvkbodsso6vtfmpcagjtjoqdusq'
vault_host = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaa7cw476u7eebw62gya4k6kgc4soirh46hngleak3dnsma'

response = secrets_client.get_secret_bundle(vault_user)
vault_user_value = response.data.secret_bundle_content.content
oci_dbsystem_user = base64.b64decode(vault_user_value).decode('utf-8')

response = secrets_client.get_secret_bundle(vault_password)
vault_password_value = response.data.secret_bundle_content.content
oci_dbsystem_password = base64.b64decode(vault_password_value).decode('utf-8')

response = secrets_client.get_secret_bundle(vault_database)
vault_database_value = response.data.secret_bundle_content.content
oci_dbsystem_database = base64.b64decode(vault_database_value).decode('utf-8')

response = secrets_client.get_secret_bundle(vault_host)
vault_host_value = response.data.secret_bundle_content.content
oci_dbsystem_host = base64.b64decode(vault_host_value).decode('utf-8')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/libros')
def libros():
    conn = mysql.connector.connect(
        host=oci_dbsystem_host,
        user=oci_dbsystem_user,
        password=oci_dbsystem_password,
        database=oci_dbsystem_database)
    
    c = conn.cursor()
    c.execute("SELECT * FROM Books")
    books = c.fetchall()
    conn.close()
    return render_template("libros.html", books=books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
