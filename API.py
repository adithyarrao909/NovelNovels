# API.py - Handle API requests and data retrieval

import requests
from sysdefs import GBOOKS_API_KEY  # Import the Google Books API key from sysdefs module
from sysdefs import Books_c

def get_open_library_books(query):
    # Open Library API endpoint for book search
    url = "https://openlibrary.org/search.json"
    
    # Set up the parameters for the API request
    params = {"q": query}
    
    # Make the API request to Open Library
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()

        # Check if "docs" key exists in the API response
        if "docs" in result:
            return result["docs"]
        else:
            print("No books found in the API response.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# def get_reviews_andpgcnt_google_books(api_key, query, max_results=1):
#     base_url = "https://www.googleapis.com/books/v1/volumes"
    
#     # Set up the parameters for the API request
#     params = {
#         'q': query,
#         'key': api_key,
#         'maxResults': max_results
#     }

#     # Make the API request to Google Books
#     response = requests.get(base_url, params=params)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()

#         # Check if there are any items in the response
#         if 'items' in data and data['items']:
#             # Print the titles and authors of the books
#             for item in data['items']:
#                 volume_info = item['volumeInfo']
#                 title = volume_info['title']
#                 authors = volume_info.get('authors', ['Unknown'])
#                 print(f"Title: {title}")
#                 print(f"Authors: {', '.join(authors)}")
#                 print("----")
#         else:
#             print(f"No results found for '{query}'.")
#     else:
#         print(f"Error: {response.status_code}")
