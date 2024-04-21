from interactions import Client
from quart import Quart

def Webserver(app: Quart, bot: Client):
    @app.route("/")
    async def root():
        return "The Emulation webserver is alive & responding."
    
    # registering all of the endpoints & webhooks we have 
    from .endpoints.users import UserInfo
    
    UserInfo(app, bot)