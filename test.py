from colorama import init, Fore, Style
import requests
import spacy

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

def find_most_similar_rated_books(user_input, books, top_n=10):
    nlp = spacy.load("en_core_web_md")
    user_input_embedding = nlp(user_input).vector

    # Filter books with ratings
    rated_books = [book for book in books if "ratings_average" in book]
    
    # Sort books by ratings in descending order
    sorted_books = sorted(rated_books, key=lambda x: x.get("ratings_average", 0), reverse=True)
    
    # Take the top N rated books
    top_rated_books = sorted_books[:top_n]

    print(Fore.YELLOW + f"\nTop {top_n} Rated Books:" + Style.RESET_ALL)
    for i, book in enumerate(top_rated_books, start=1):
        print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
        print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
        print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
        print()

    most_similar_rated_books = []

    for book in top_rated_books:
        if "title" in book and "author_name" in book and "subject_key" in book:
            book_title = book["title"]
            book_embedding = nlp(book_title).vector
            similarity = (
                nlp(" ".join(book["author_name"])).similarity(nlp(user_input)) +
                nlp(" ".join(book["author_name"])).similarity(nlp(book_title)) +
                nlp(book_title).similarity(nlp(user_input))
            )
            most_similar_rated_books.append({"similarity": similarity, "book": book})

    # Sort the most similar books by similarity in descending order
    most_similar_rated_books = sorted(most_similar_rated_books, key=lambda x: x["similarity"], reverse=True)

    return most_similar_rated_books[:5]

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama for colored output
    
    user_input = input("Enter a string: ")
    books = get_open_library_books(user_input)

    if books:
        most_similar_rated_books = find_most_similar_rated_books(user_input, books, top_n=10)

        if most_similar_rated_books:
            print(Fore.GREEN + "\nTop 5 Most Similar and Rated Books:" + Style.RESET_ALL)
            for i, book_info in enumerate(most_similar_rated_books, start=1):
                book = book_info["book"]
                print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
                print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
                print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
                print(f"   {Fore.CYAN}Similarity Score:{Style.RESET_ALL} {book_info['similarity']:.2f}")
                print()
        else:
            print(Fore.RED + "No similar and rated books found." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No books found for the entered string." + Style.RESET_ALL)






# def get_open_library_book_subjects():
#     url = "http://openlibrary.org/people/george08/lists/OL97L/subjects.json?limit=200"
#     url1
#     response = requests.get(url)
#     response = requests.get(url1)
#     data = []


#     if response.status_code == 200:
#         result = response.json()
#         if "subjects" in result:
#             for work in result["subjects"]:
#                 data.append(work["name"])
#                 print(data)
#             return list(data)
#         else:
#             print("No subjects found in the API response.")
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)

#     if response1.status_code == 200:
#         result = response1.json()
#         if "subjects" in result:
#             for work in result["subjects"]:
#                 data.append(work["name"])
#                 print(data)
#             return list(data)
#         else:
#             print("No subjects found in the API response.")
#     else:
#         print(f"Error: {response1.status_code}")
#         print(response1.text)

# if __name__ == "__main__":
#     book_subjects = get_open_library_book_subjects()

#     if book_subjects:
#         print("Book Subjects:")
#         for subject in book_subjects:
#             print(f"- {subject}")




# # class UserInterface:
#     @staticmethod
#     def get_user_input():
#         init(autoreset=True)  # Initialize colorama for colored output

#         responses = []

#         # Ask the user about the genre
#         genre_response = input("What kind of book does your heart seek? ")
#         if (genre_finder(genre_response)):
#             responses.append(genre_response)

#         # Call keyword_function("genre") and store the returned data
#         # Assuming you have a function named keyword_function, replace it with your actual implementation
#         genre_data = keyword_function("genre")
#         responses.append(f"Retrieved data for {genre_response}: {genre_data}")

#         # Ask the user about their impression of the genre
#         impression_response = input(f"How does {genre_response} sound? ")
#         responses.append(impression_response)

#         # Check if the response is negative
#         if any(negative_word in impression_response.lower() for negative_word in ["bad", "not good", "no", "nah"]):
#             # Ask about the desired book length
#             length_response = input("How long of a length book are you looking for? ")
#             responses.append(length_response)

#         return responses

#     @staticmethod
#     def display_responses(responses):
#         print("\nUser Responses:")
#         for response in responses:
#             print(response)


# # Example usage
# # if __name__ == "__main__":
# #     user_responses = UserInterface.get_user_input()
# #     UserInterface.display_responses(user_responses)
