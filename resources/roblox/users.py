from dataclasses import dataclass 
from rblxopencloud import ApiKey
from resources.config import OPENCLOUD_GROUP_SECRET

secret_handler = ApiKey(str(OPENCLOUD_GROUP_SECRET))

@dataclass 
class RobloxUser:
    """Representation of a user on Roblox."""
    cachedUsername: str 
    discord_id: str 
    roblox_id: str
    
    def get_user_object(self):
        print(self.cachedUsername, self.roblox_id, self.discord_id)
        return secret_handler.get_user(self.roblox_id, fetch_info=True)

    def get_thumbnail_url(self):
        return self.get_user_object().generate_headshot(420, "png", False).wait()  
    
    def get_account_age(self):
        return self.get_user_object().created_at
    
    def fetch_member(self, group_id: int):
        user_obj = self.get_user_object()
        
        for group_obj in user_obj.list_groups():
            if group_obj.group.id == group_id:
                return group_obj
            
        return None
