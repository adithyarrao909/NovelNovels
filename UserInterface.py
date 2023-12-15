from colorama import init, Fore, Style
import sysdefs

def get_book_info(book):
    return f"Title: {book['title']}\nAuthor: {', '.join(book.get('author_name', []))}\nRating: {book.get('ratings_average', 'N/A')}"


def print_books(books, title_color=Fore.CYAN, author_color=Fore.YELLOW, rating_color=Fore.MAGENTA):

    for i, book in enumerate(books, start=1):
        # print(f"{i}. {title_color}Title:{Style.RESET_ALL} {book['title']}")
        print(f"   {author_color}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
        print(f"   {rating_color}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
        print()

def ui(top_rated_books, most_similar_rated_books):
    print(Fore.YELLOW + f"\nTop {sysdefs.TOP_RATED} Rated Books:" + Style.RESET_ALL)
    for i, book in enumerate(top_rated_books, start=1):
        print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
        print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
        print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
        print()

    print(Fore.GREEN + "\nTop 5 Most Similar and Rated Books:" + Style.RESET_ALL)
    for i, book_info in enumerate(most_similar_rated_books, start=1):
        book = book_info["book"]
        print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
        print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
        print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
        print(f"   {Fore.CYAN}Similarity Score:{Style.RESET_ALL} {book_info['similarity']:.2f}")
        print()

    user_choice = input("Enter the number of the book for more info (or 'exit' to quit): ")
    while user_choice.lower() != 'exit':
        try:
            user_choice = int(user_choice)
            if 1 <= user_choice <= 15:
                if user_choice <= 10:
                    book = top_rated_books[user_choice - 1]
                else:
                    book = most_similar_rated_books[user_choice - 11]
                print(Fore.CYAN + "\nBook Information:" + Style.RESET_ALL)
                print(get_book_info(book))
            else:
                print("Invalid choice. Please enter a number between 1 and 15.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        user_choice = input("Enter the number of the book for more info (or 'exit' to quit):")