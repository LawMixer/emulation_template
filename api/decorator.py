from quart import request
from functools import wraps
from resources.config import EMULATION_API_KEY


def check_auth(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        auth = request.authorization
        
        if auth != None:
            if auth.token != None or EMULATION_API_KEY != None:
                if auth.token == EMULATION_API_KEY:
                    return await func(*args, **kwargs)
            
        
        return {"error": 401, "message": "You are not authorized to use this endpoint."}
    return wrapper