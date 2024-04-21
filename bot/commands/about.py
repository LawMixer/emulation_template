from interactions import (
    Client, 
    Extension, 
    slash_command, 
    InteractionContext, 
    Embed, 
    listen, 
    events
)

class AboutUs(Extension):
    @listen() 
    async def on_startup(self, event: events.Startup):
        self.bot: Client = self.bot

    @slash_command(name="about", description="information about this group")
    async def about(self, ctx: InteractionContext):
        await ctx.defer()

        latency = round(self.bot.latency, 2)
        
        embed = Embed("Meet Emulation")
        embed.add_field("What is Emulation?", "Emulation is the multi-purpose discord bot that manages Project: Ethos for Orosius Laboratories. More information on our [website](https://usrc.orosiuslabs.com/)")
        
        embed.add_field(name="User", value=f"{self.bot.app.name} ``{self.bot.app.id}``")
        embed.add_field(name="Latency", value=latency)
        
        embed.set_thumbnail(self.bot.user.avatar_url)
        
        return await ctx.send(embeds=embed)

        
def setup(client):
    AboutUs(client)