import redis


class Redis:
    def __init__(self):
        self.redisConnection = self.connect_redis()
    
    def connect_redis(self):
        return redis.Redis(
            port=6379, 
            host="", 
            username="",
            password="", 
            decode_responses=True
        )
    
    def get_key(self, keyName: str):
        if self.redisConnection == None: return print("Redis is not started")
        
        return self.redisConnection.get(keyName)
    def set_key(self, keyName: str, keyValue: str):
        if self.redisConnection == None: return print("Redis is not started")
        
        return self.redisConnection.set(keyName, keyValue)