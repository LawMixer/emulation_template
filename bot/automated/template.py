from interactions import Client, Extension, events, listen

class InteractionExtTemplate(Extension):
    @listen() 
    async def on_startup(self, event: events.Startup):
        self.bot: Client = self.bot      
                
def setup(client):
    InteractionExtTemplate(client)