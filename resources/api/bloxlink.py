import firebase_admin, requests 

from rblxopencloud import User
from firebase_admin import db 
from resources.config import BLOXLINK_API_KEY, OPENCLOUD_GROUP_SECRET

scpfdata = firebase_admin.get_app("example-app")

class Bloxlink:
    """External Verification by Bloxlink"""
    """Still working on fully implementing ratelimit toggle"""
    
    def __init__(self):
        self.guild_id = 864557936068395018
        
        self.base_url = f"https://api.blox.link/v4/public/guilds/{self.guild_id}/discord-to-roblox"
        self.isRatelimited = False 
    async def get_roblox_info(self, discord_id):
        if self.isRatelimited == True:
            return "Couldn't connect to the API right now, try again later."
        try:
            result = requests.get(f"{self.base_url}/{discord_id}",
                headers={'Content-Type':'application/json',
               'Authorization': f'{BLOXLINK_API_KEY}'})
            

            assert(result.status_code == 200)
        except AssertionError as r:
            r = result.json()

            print(r)
            return False, r
        else:
            newJson = result.json()
            user = User(newJson["robloxID"], OPENCLOUD_GROUP_SECRET)

            users = db.reference("Users", app=scpfdata)
            users.update({
                newJson["robloxID"]: {
                "cachedUsername": user.id, 
                "roblox_id": newJson["robloxID"],
                "discord_id": discord_id
                }
            })

            return True, None