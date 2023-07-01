import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_reviews(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        reviews = data["result"].get("reviews", [])
        return reviews
    else:
        print("Failed to retrieve reviews.")
        return []

def extract_top_reviews(place_name):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&fields=place_id&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        candidates = data["candidates"]
        if candidates:
            place_id = candidates[0]["place_id"]
            reviews = get_reviews(place_id)
            return reviews[:50]
        else:
            print("Place not found.")
    else:
        print("Failed to retrieve place details.")
    return []

# usage
place_name = input("Enter the place name: ")
top_reviews = extract_top_reviews(place_name)

for i, review in enumerate(top_reviews, start=1):
    print(f"Review {i}:")
    print(f"Rating: {review['rating']}")
    print(f"Author: {review['author_name']}")
    print(f"Text: {review['text']}")
    print()
