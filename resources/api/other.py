import requests 


class regexGenerator:
    def get_regex(self, keyword: str, bit_wise):        
        if keyword == "" or keyword == None:
            return "You need to provide a keyword"
        
        url = f"https://automod-regex-generator-api.treeben77.xyz/leetspeak/{keyword}"
        response = requests.get(url, params={"settings": bit_wise})
        
        return response.json()