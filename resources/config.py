from os import environ
from dotenv import load_dotenv
load_dotenv()
    
    
# Env vars won't work, unless there's an .env file
PROD_ENV = environ.get("PROD_ENV")
IS_PROD = environ.get("IS_PROD")
IS_TESTING = environ.get("IS_TESTING") 

BLOXLINK_API_KEY = environ.get("BLOXLINK_API_KEY") 

# Personal Secrets
EMULATION_API_KEY = environ.get("EMULATION_API_KEY")

# OpenCloud API Keys
OPENCLOUD_DATASTORE_SECRET = environ.get("OPENCLOUD_DATASTORE_SECRET") 
OPENCLOUD_GROUP_SECRET = environ.get("OPENCLOUD_GROUP_SECRET") 