import os
import requests
import json
from nail_salon_marketplace_scraper import app

# Your Google Places API key
#API_KEY = os.getenv('API_KEY')
API_KEY = app.config["GOOGLE_MAPS_API_KEY"]

def get_places(query, page_size=50):
    """
    Searches for places based on a text query and returns a list of place IDs.
    https://developers.google.com/maps/documentation/places/web-service/place-details

    Args:
        query (str): The search text query (e.g., "nail salon in new york city").
        page_size (int): The number of results to return (default is 5).

    Returns:
        list: A list of place IDs.
    """
    url = "https://places.googleapis.com/v1/places:searchText"
    headers = {
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "places.id,nextPageToken",
        "Content-Type": "application/json"
    }
    data = {
        'textQuery': query,
        'pageSize': page_size
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        places = response.json().get('places', [])
        place_ids = [place['id'] for place in places]
        return place_ids
    else:
        # TODO: SETUP MONITORING
        print(f"Error: {response.status_code}")
        print(response.text)
        return []


def get_place_details(place_id):
    """
    Retrieves detailed information for a specific place by its ID.

    Args:
        place_id (str): The ID of the place to retrieve details for.

    Returns:
        dict: A dictionary containing detailed information about the place.
    """
    place_info_url = f"https://places.googleapis.com/v1/places/{place_id}"
    headers = {
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": "id,displayName,currentOpeningHours,websiteUri,formattedAddress,googleMapsUri,nationalPhoneNumber"
    }

    response = requests.get(place_info_url, headers=headers)
    if response.status_code == 200:
        place_info = response.json()
        breakpoint()
        return place_info
    else:
        # TODO: SETUP MONITORING
        print(f"Error: {response.status_code}")
        print(response.text)
        return {}


# Example usage
if __name__ == "__main__":
    # Step 1: Get a list of places based on a text query
    place_ids = get_places("nail salon in new york city")

    if place_ids:
        # Step 2: Get details for the first place in the list
        place_details = get_place_details(place_ids[0])
        print("Place Details:", place_details)
    else:
        print("No places found.")
