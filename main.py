import glob, logging  

from interactions import Intents, listen, events
from quart.logging import default_handler
from quart import Quart 

from bot.bot import CustomClient
from resources.config import IS_PROD, APP_BIND
from api.webserver import Webserver


client = CustomClient(token=IS_PROD, intents=Intents.ALL)
app = Quart(__name__)

for filename in glob.glob("bot/**/*.py"):
    client.load_extension(filename.replace(".py", "").replace("/", "."))

@listen()
async def on_ready(event: events.Ready):
    from hypercorn.config import Config
    from hypercorn.asyncio import serve
    
    config = Config()
    config.bind = [APP_BIND]
    logging.getLogger().removeHandler(default_handler)
    
    
    client.ws.loop.set_debug(False)    
    client.ws.loop.create_task(serve(app, config))
    Webserver(app, client)

client.start()