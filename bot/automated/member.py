from interactions import (
    listen, 
    Extension, 
    Client, 
    events
) 

class MemberEvents(Extension):
    @listen() 
    async def on_startup(self, event: events.Startup):
        self.bot: Client = self.bot
        self.guild = await self.bot.fetch_guild(864557936068395018)    
        self.channel = await self.guild.fetch_channel(1088885080237277294)
        
        self.unauth_role = self.guild.get_role(1106563044248657971)
        self.auth_role = self.guild.get_role(1091834304776130581)
        self.sys_role = await self.guild.fetch_role(874709930861559839)
    @listen()
    async def onGuildMemberJoin(self, event: events.MemberAdd):
        msgFormat = f"Welcome {event.member.user.mention} to <:orosius:1137561309555200000>**Orosius Laboratories**, we are now at **{self.guild.member_count}** members."
            
        await self.channel.send(msgFormat)
    @listen()
    async def onBoosterRoleAdd(self, event: events.MemberUpdate):
        booster_role = event.guild.get_role(875786221018841181)
        
        if booster_role in event.after.roles:
            print("somebody boosted the server!")
            
            await self.channel.send(f"Thank you, {event.after.mention} for boosting our server! :tada:")
            
            


def setup(client):
    MemberEvents(client)