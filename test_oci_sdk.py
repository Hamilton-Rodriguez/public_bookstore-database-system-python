import oci

config = oci.config.from_file("/home/opc/.oci/config")
identity = oci.identity.IdentityClient(config)
compartments = identity.list_compartments(config["tenancy"]).data

for compartment in compartments:
    print(compartment.name, compartment.id)