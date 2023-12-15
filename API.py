# API.py - Handle API requests and data retrieval

import requests
from sysdefs import GOODREADS_API_KEY

def get_open_library_books(query):
    url = "https://openlibrary.org/search.json"
    params = {"q": query}
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        result = response.json()
        if "docs" in result:
            return result["docs"]
        else:
            print("No books found in the API response.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)