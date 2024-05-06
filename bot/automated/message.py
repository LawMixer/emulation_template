from interactions import (
    listen, 
    Extension, 
    Client, 
    events, 
    Embed, 
    ChannelType 
)

class onMessage(Extension):
    @listen() 
    async def on_startup(self, event: events.Startup):
        self.bot: Client = self.bot
        self.guild = await self.bot.fetch_guild(864557936068395018)    
        self.channel = await self.guild.fetch_channel(1098015834330365962)
    
    @listen()
    async def on_message_delete(self, event: events.MessageDelete):
        if not event.message.content and not event.message.embeds:
            return 

        embed = Embed("An event was triggered", f"{event.message.author.mention} ``{event.message.author.id}`` triggered {event.resolved_name}, check below for the details.")
        embed.add_field("Action:", "Deleted Message", inline=True)
        embed.add_field("Original Content", f"```{event.message.content}```", inline=True)
        
        await self.channel.send(embeds=embed)
    @listen()
    async def on_message_update(self, event: events.MessageUpdate):
        if not event.message.content and not event.message.embeds:
            return 
            
        embed = Embed("An event was triggered", f"{event.message.author.mention} ``{event.message.author.id}`` triggered {event.resolved_name}, check below for the details.")
        embed.add_field("Action:", "Message Updated")
        embed.add_field("Message Before", f"```{event.after.content}```", inline=True)
        embed.add_field("Message After", f"```{event.after.content}```", inline=True)
            
        await self.channel.send(embeds=embed)
        
    @listen()
    async def on_message_create(self, event: events.MessageCreate):
        if event.message.channel.type == ChannelType.GUILD_NEWS:
            await event.message.publish()

def setup(client):
    onMessage(client)