# main() function for the Novelnovels program

import sysdefs
import API
import RecAlgorithm
import UserInterface

from colorama import init, Fore, Style

if __name__ == "__main__":
    popular_rec_toggle = 0
    init(autoreset=True)  # Initialize colorama for colored output
    while(1):
        user_input = input("Would you like your books to be sorted by popularity?(y/n): ")
        if (user_input in {"Y", "y"}):
           popular_rec_toggle = 1
           break
        elif (user_input in {"N", "n"}):
           popular_rec_toggle = 0
           break
        else:
            print("Invalid input! Try again")
    while(1):
        pgcnt_user_input = input("How many pages? (0=0:250, 1=250:500, 2=500:10000): ")
        if (pgcnt_user_input in {"0", "1", "2"}):
            break
        else:
            print("Invalid input! Try again")

    genre_user_input = input("What genre are you feeling? (try to be accurate with spelling): ")
    # user_input = input("Include any other keywords/descriptions of the movie you want separated by a space: ")

    books = API.get_open_library_books(genre_user_input)

    if books:
        top_rated_books = sorted([book for book in books if "ratings_average" in book], key=lambda x: x.get("ratings_average", 0), reverse=True)[:100]
        top_rated_books = top_rated_books[:int(sysdefs.TOP_RATED)]
        most_similar_rated_books = RecAlgorithm.find_most_similar_rated_books(user_input, books, popular_rec_toggle, top_n=int(sysdefs.TOP_RATED))

        if top_rated_books and most_similar_rated_books:
            UserInterface.ui(top_rated_books, most_similar_rated_books)
        else:
            print(Fore.RED + "No similar and rated books found." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No books found for the entered string." + Style.RESET_ALL)
