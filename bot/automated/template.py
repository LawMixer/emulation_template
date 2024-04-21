from interactions import Client, Extension, events, listen

class InteractionExtTemplate(Extension):
    @listen() 
    async def on_startup(self, event: events.Startup):
        self.bot: Client = self.bot
    
    @listen()
    async def on_message_delete(self, event: events.MessageDelete):        
        if hasattr(event, "message") == False: 
            return 
        
        if hasattr(event.message, "content") == False:
            return

        print("the event was triggered")
    @listen()
    async def onGuildMemberJoin(self, event: events.MemberAdd):
        print("somebody joined the server")
    
    @listen()
    async def onBoosterRoleAdd(self, event: events.MemberUpdate):
        booster_role = event.guild.get_role(875786221018841181)
        
        if booster_role in event.after.roles:
            print("somebody boosted the server!")            
                
def setup(client):
    InteractionExtTemplate(client)