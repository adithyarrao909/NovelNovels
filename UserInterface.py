from colorama import init, Fore, Style
import sysdefs
import API
import DetailedView

def bookshelf_display(strings):
     # Define colors
    colors = ["\033[1;31m", "\033[1;32m", "\033[1;33m"]

    # Determine the maximum length of strings in each column
    max_lengths = [max(len(strings[i + j * 3]) for i in range(min(3, len(strings) - j * 3))) for j in range(len(colors))]

    # Print the header
    print("\033[1mFancy List:\033[0m")

    # Display the first 3 strings in each column with proper tabulation and alignment
    for i in range(min(3, len(strings))):
        for j, color in enumerate(colors):
            index = i + j * 3
            if index < len(strings):
                padding = max_lengths[j] - len(strings[index]) + 1
                print(f"{color}• {strings[index]}{' ' * padding}\033[0m", end="\t")
        print()  # Move to the next line after each row

def display_list_in_columns(strings):
    max_length = max(len(s) for s in strings)
    border = '+' + '-' * (max_length + 10) + '+'

    # Print the heading
    heading = "Book themes:"
    print(f"\n{heading:^{max_length + 10}}\n")

    print(f"{border:<{max_length + 10}}{border}")
    
    # Determine the midpoint index
    midpoint = len(strings) // 2
    
    # Define colors for bullet points
    bullet_colors = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]

    # Iterate over the pairs of strings
    for i, (left, right) in enumerate(zip(strings[:midpoint], strings[midpoint:])):
        bullet_color = bullet_colors[i % len(bullet_colors)]
        print(f"| {bullet_color}•\033[0m {left:<{max_length}} | {bullet_color}•\033[0m {right:<{max_length}} |")

    # If the number of strings is odd, print the last one alone
    if len(strings) % 2 != 0:
        bullet_color = bullet_colors[-1]
        print(f"| {bullet_color}•\033[0m {strings[-1]:<{max_length}} | {' ' * (max_length + 2)} |")

    print(f"{border:<{max_length + 10}}{border}")


def get_book_info(book):  
    return f"Title: {book['title']}\nAuthor: {', '.join(book.get('author_name', []))}\nRating: {book.get('ratings_average', 'N/A')}\n"


def ui(top_rated_books, most_similar_rated_books):
    print(Fore.YELLOW + f"\nTop {sysdefs.TOP_RATED} Rated Books:" + Style.RESET_ALL)
    for i, book in enumerate(top_rated_books, start=1):
        print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
        print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
        print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
        print()
        print("")

    print(Fore.GREEN + "\nTop 5 Most Similar and Rated Books:" + Style.RESET_ALL)
    for i, book_info in enumerate(most_similar_rated_books, start=1):
        book = book_info["book"]
        print(f"{i}. {Fore.CYAN}Title:{Style.RESET_ALL} {book['title']}")
        print(f"   {Fore.CYAN}Author:{Style.RESET_ALL} {', '.join(book.get('author_name', []))}")
        print(f"   {Fore.CYAN}Rating:{Style.RESET_ALL} {book.get('ratings_average', 'N/A')}")
        print(f"   {Fore.CYAN}Similarity Score:{Style.RESET_ALL} {book_info['similarity']:.2f}")
        print()

    
    print(Fore.YELLOW + "\n#1 Recommended Book for you:" + Style.RESET_ALL)
    print(get_book_info(most_similar_rated_books[0]['book']))
    display_list_in_columns(most_similar_rated_books[0]['book']['subject'][:5])

    user_choice = input("Enter the number of the book for more info (or 'exit' to quit): ")
    while user_choice.lower() != 'exit':
        try:
            user_choice = int(user_choice)
            if(0 < int(user_choice) <= 5):
                book = most_similar_rated_books[user_choice - 1]
                print(Fore.CYAN + "\nBook Information:" + Style.RESET_ALL)
                print(get_book_info(book['book']))
                display_list_in_columns(book['book'].get('subject')[:5])
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        user_choice = input("Enter the number of the book for more info (or 'exit' to quit):")