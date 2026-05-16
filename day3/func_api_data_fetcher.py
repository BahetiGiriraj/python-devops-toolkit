import requests
import json


api_url = "https://dadjokes.bamboozledaardvark.com/api/jokes/random"

def joke_fetch():
    try:

        response = requests.get(api_url)
        joke_data = response.json()
        only_joke = joke_data["joke"]
        with open("only_joke.txt", "w") as file:
            file.write(only_joke)
        with open("only_joke.json", "w") as file:
            json.dump(only_joke, file, indent=4)
    except Exception as e : 
        print(f"An error occurred while fetching the joke: {e}")

joke_fetch()

    

