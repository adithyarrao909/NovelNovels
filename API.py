# API.py - Handle API requests and data retrieval

import requests
from sysdefs import GBOOKS_API_KEY

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

def get_reviews_andpgcnt_google_books(api_key, query, max_results=1):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    
    # Set up the parameters for the API request
    params = {
        'q': query,
        'key': api_key,
        'maxResults': max_results
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are any items in the response
        if 'items' in data and data['items']:
            # Print the titles and authors of the books
            for item in data['items']:
                volume_info = item['volumeInfo']
                title = volume_info['title']
                authors = volume_info.get('authors', ['Unknown'])
                print(f"Title: {title}")
                print(f"Authors: {', '.join(authors)}")
                print("----")
        else:
            print(f"No results found for '{query}'.")
    else:
        print(f"Error: {response.status_code}")

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual Google Books API key
    search_query = 'machine learning'  # Replace with your search query

    search_books(api_key, search_query)
