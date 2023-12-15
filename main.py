# main() function for the Novelnovels program

import sysdefs
import API
import RecAlgorithm
import UserInterface

from colorama import init, Fore, Style

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama for colored output
    
    user_input = input("Enter a string: ")
    books = API.get_open_library_books(user_input)
    print(books)

    if books:
        top_rated_books = sorted([book for book in books if "ratings_average" in book], key=lambda x: x.get("ratings_average", 0), reverse=True)[:100]
        top_rated_books = top_rated_books[:int(sysdefs.TOP_RATED)]
        most_similar_rated_books = RecAlgorithm.find_most_similar_rated_books(user_input, books, top_n=int(sysdefs.TOP_RATED))

        if top_rated_books and most_similar_rated_books:
            # UserInterface.ui(top_rated_books, most_similar_rated_books)
            print("REMOVE THIS")
        else:
            print(Fore.RED + "No similar and rated books found." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No books found for the entered string." + Style.RESET_ALL)
