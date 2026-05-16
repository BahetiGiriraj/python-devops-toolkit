import requests
import json

api_url = "https://dadjokes.bamboozledaardvark.com/api/jokes/random"


response = requests.get(api_url)
joke_data = response.json()
print(f"Joke: {joke_data['joke']}")
only_joke = joke_data['joke']
with open('only_joke.json', "w") as file:
        json.dump(only_joke, file, indent=4)
        
        
   
    




"""
json.dump = write directly to a file
json.dumps = convert to a string
indent = adds indentation to the JSON data for better readability

"""