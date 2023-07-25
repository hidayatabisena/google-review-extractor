import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_place_id(place_name):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={place_name}&inputtype=textquery&fields=place_id&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        candidates = data.get("candidates", [])
        if candidates:
            return candidates[0]["place_id"]
        else:
            print("Place not found.")
    else:
        print("Failed to retrieve place details.")
    return None

def get_reviews(place_id, max_results=50):
    all_reviews = []
    offset = 0

    while len(all_reviews) < max_results:
        url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}&offset={offset}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "OK":
            reviews = data["result"].get("reviews", [])
            num_remaining = max_results - len(all_reviews)
            all_reviews.extend(reviews[:num_remaining])

            if len(reviews) < num_remaining:
                # Fewer reviews returned than remaining needed
                break
            else:
                offset += num_remaining
        else:
            print("Failed to retrieve reviews.")
            break

    return all_reviews[:max_results]

def extract_reviews(place_name):
    place_id = get_place_id(place_name)
    if place_id:
        reviews = get_reviews(place_id)
        return reviews
    else:
        return []

# usage
place_name = input("Enter the place name: ")
reviews = extract_reviews(place_name)

for i, review in enumerate(reviews, start=1):
    print(f"Review {i}:")
    print(f"Rating: {review['rating']}")
    print(f"Author: {review['author_name']}")
    print(f"Text: {review['text']}")
    print()