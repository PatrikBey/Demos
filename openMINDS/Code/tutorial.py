import openMINDS
import openMINDS.version_manager

# Initialise the local copy of openMINDS
openMINDS.version_manager.init()

# Select which version of openMINDS to use
openMINDS.version_manager.version_selection('v2.0.0')

# initiate the helper class for the dynamic usage of a specific openMINDS version
helper = openMINDS.Helper()

# initiate the collection into which you will store all metadata instances
mycollection = helper.create_collection()

# create a metadata instance for (e.g.) the openMINDS Person schema
person_open = mycollection.add_core_person(givenName="open")

# add more metadata to a created instance
mycollection.get(person_open).familyName = "MINDS"

# add connections to other metadata instances
email_openminds = mycollection.add_core_contactInformation(email="openminds@ebrains.eu")
mycollection.get(person_open).contactInformation = email_openminds

# save your collection
mycollection.save("./myFirstOpenMINDSMetadataCollection/")

# Getting help for properties
mycollection.help_core_actors_person()