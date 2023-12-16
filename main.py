# main() function for the Novelnovels program

# Import necessary modules
import sysdefs  # Custom module with system definitions
import API  # Module handling API requests and data retrieval
import RecAlgorithm  # Module implementing recommendation algorithms
import UserInterface  # Module for user interface
from sysdefs import Books_c

from colorama import init, Fore, Style  # Colorama for colored output

if __name__ == "__main__":
    # Initialize colorama for colored output
    init(autoreset=True)

    # Initialize toggle for sorting by popularity
    popular_rec_toggle = 0

    # Initialize local data structs
    SingleBook = Books_c

    while True:
        # Prompt user for sorting preference by popularity
        user_input = input("Would you like your books to be sorted by popularity? (y/n): ")

        # Process user input for sorting preference
        if user_input.lower() in {"y", "yes"}:
            popular_rec_toggle = 1
            break
        elif user_input.lower() in {"n", "no"}:
            popular_rec_toggle = 0
            break
        else:
            print("Invalid input! Try again")

    # Prompt user for the desired book genre
    genre_user_input = input("What genre/vibe/topic are you feeling? (keep it concise; spelling matters): ")

    # Retrieve books from the Open Library API based on the specified genre
    books = API.get_open_library_books(genre_user_input)

    if books:
        # Filter and sort top rated books from the retrieved books
        top_rated_books = sorted(
            [book for book in books if "ratings_average" in book],
            key=lambda x: x.get("ratings_average", 0),
            reverse=True
        )[:100]
        
        # Limit the number of top-rated books based on the sysdefs module
        top_rated_books = top_rated_books[:int(sysdefs.TOP_RATED)]

        for i, book in enumerate(top_rated_books, start=1):
            print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
            print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
            print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
            print()
            print("")

        # Find most similar rated books using recommendation algorithm
        most_similar_rated_books = RecAlgorithm.find_most_similar_rated_books(
            user_input,
            books,
            popular_rec_toggle,
            top_n=int(sysdefs.TOP_RATED)
        )

        # Data is fully filtered and usable at this point

        # Display user interface with top-rated and similar books
        if top_rated_books and most_similar_rated_books:
            UserInterface.ui(top_rated_books, most_similar_rated_books)
        else:
            print(Fore.RED + "No similar and rated books found." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No books found for the entered string." + Style.RESET_ALL)
