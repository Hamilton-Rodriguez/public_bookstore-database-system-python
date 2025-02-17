from flask import Flask, render_template
import mysql.connector
import oci
import base64

app = Flask(__name__)

config = oci.config.from_file("/home/opc/.oci/config")  # Assumes default config file location: ~/.oci/config
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
#secrets_client = oci.secrets.SecretsClient(config)
# Initialize the SecretsClient with the Instance Principal signer
secrets_client = oci.secrets.SecretsClient(config={}, signer=signer)

host_secret_id = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaa7cw476u7eebw62gya4k6kgc4soirh46hngleak3dnsma'
user_secret_id = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaagc67tpnxo3yb7g5wplsiycihsabjmc56g7cwnk2zgy5a'
password_secret_id = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaagctdfqix6ohnctyc4tuz6qegrrk5bcqnsdv5lqxvubmq'
database_secret_id = 'ocid1.vaultsecret.oc1.sa-bogota-1.amaaaaaav3pognaadbqyfmh763jgl33tpbvkbodsso6vtfmpcagjtjoqdusq'

""" def get_secret_value(secret_id):
    secret_content = secrets_client.get_secret_bundle(secret_id).data.secret_bundle_content
    secret_value = secret_content.content.decode('utf-8')
    return secret_value """

def get_secret_value(secret_id):
    secret_bundle = secrets_client.get_secret_bundle(secret_id).data
    secret_value = base64.b64decode(secret_bundle.secret_bundle_content.content).decode('utf-8')
    return secret_value

""" oci_dbsystem_host = get_secret_value(host_secret_id)
oci_dbsystem_user = get_secret_value(user_secret_id)
oci_dbsystem_password = get_secret_value(password_secret_id)
oci_dbsystem_database = get_secret_value(database_secret_id) """


#################

# Retrieving and displaying the database connection parameters
oci_dbsystem_host = get_secret_value(host_secret_id)
print("Database Host:", oci_dbsystem_host)

oci_dbsystem_user = get_secret_value(user_secret_id)
print("Database User:", oci_dbsystem_user)

oci_dbsystem_password = get_secret_value(password_secret_id)
print("Database Password:", oci_dbsystem_password)

oci_dbsystem_database = get_secret_value(database_secret_id)
print("Database Name:", oci_dbsystem_database)

#################



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

