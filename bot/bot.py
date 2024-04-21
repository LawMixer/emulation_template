import traceback

from interactions import (
    Client, 
    listen, 
    errors, 
    events 
)

def format_seconds(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{hour}:{minutes}:{seconds}"

class CustomClient(Client):
    @listen(is_default_listener=True)
    async def on_command_error(self, event: events.CommandError):
        if isinstance(event.error, errors.CommandOnCooldown):
            formatted_seconds = format_seconds(round(event.error.cooldown.get_cooldown_time()))
            await event.ctx.send(f"You are on cooldown. Try again in {formatted_seconds} seconds")
            return 
        
        print("[DEBUG]: ", event.error)
        trace_back = traceback.format_exception(event.error)
        print("\n" if len(trace_back) > 1 else " ", "".join(trace_back))
    @listen()
    async def on_ready(self, event: events.Ready):
        print(f"{event.client.app.name}: Started")
    @listen()
    async def on_disconnect(self, event: events.Disconnect):        
        print(f"{event.client.app.name}: Stopped")