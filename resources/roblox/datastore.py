from rblxopencloud import Experience
from resources.config import OPENCLOUD_DATASTORE_SECRET


ethosExperience = Experience(0000000, api_key=str(OPENCLOUD_DATASTORE_SECRET))
class RobloxDatastore:
    ethosDatastore = ethosExperience.get_data_store("CreditSystem", scope="global")

    def get_entry(self, key):
        value, data = None, None
        
        try:
            value, data = self.ethosDatastore.get_entry(str(key))
        except Exception as e:
            print(e.args)
            return None

        return value
    def set_entry(self, key, data):
        self.ethosDatastore.set_entry(str(key), data)
    def remove_entry(self, key):
        if self.get_entry(key) == None: return None
        
        self.ethosDatastore.remove_entry(str(key))