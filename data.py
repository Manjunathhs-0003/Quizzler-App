import requests 

parameters = {
    "amount" : 10, 
    "type" : "boolean",
}

response = requests.get("Your API key from open trivia (for example: https://opentdb.com/api.php)", params = parameters )
response.raise_for_status()
data = response.json()
question_data = data["results"]




