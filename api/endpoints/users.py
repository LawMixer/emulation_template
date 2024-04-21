from interactions import Client 
from resources.roblox.users import RobloxUser

from api.decorator import check_auth
from quart import Quart

def UserInfo(app: Quart, bot: Client):
    
    @app.route("/users/<account_id>", methods=['GET'])
    @check_auth
    async def get_account_from_data(account_id):
        user_data = RobloxUser("something", "11111111111111", "111111111") # this will be pulled from db
                
        print(user_data)
        if user_data != None:
            return {'cachedUsername': user_data.cachedUsername, 'roblox_id': user_data.roblox_id, 'discord_id': user_data.discord_id}
        elif user_data == None:
            return {"error": "User is not linked"}
        else:
            return {"error": "Internal Server Error"}