# NovelNovels

With the immense popularity of reading as a hobby and the countless books available to read, It has become quite difficult to narrow down your choices or to find new book recommendations. Aspiring readers often face information overload with the different niches, authors, genres, etc. giving reading a barrier to entry. Novel Novels is intended to break this barrier of entry by acting as an interface between aspiring readers and the vast book data available on the internet. The program will make book recommendations based on the user’s taste and mood.

API data from Open Books is parsed and stored to form a smaller internal database upon which the NLP (natural language processing) is used to find similarities between the API data and the user input. This allows a semi-ambiguous query like "cat lasagna" to produce
results like "Garfield Fat Cat 3-Pack volume 1". The most relevant data is collected from the API and cached immediately. The data is used on the fly as the user requests certain data.

Used a free open-source library for Natural Language Processing called Spacy (first-time). 
Utilized en_core_web_md which is an English pipeline optimized for CPU.
The recommendation algorithm takes in the API response dataand filters in stages:
1) Popularity filtering is toggled if users prefer popular books, and as such is 
       sorted by popularity by measuring the total number of reader reviews. If it is not toggled,
       The data is left as is.
2) Next, it is sorted by avg rating.
3) Lastly, the NLP is given characteristics like the author_name, subject_key(series of words desecribing the book), and subject_facet(even more words describing the book).
4) A similarity rating to the user input is attributed to each book and they are sorted.
5) Finally, the most suitable book is determined and highlighted in the GUI.

The user interface has an interactive and error-resistant design. It asks only the necessary questions, giving the used a very smooth experience. An example run can be seen at the bottom of this readme.

Files:
* API.py - Handle API requests and data retrieval
* UserInterface - Handles the terminal UI that the user interacts with
* RecAlgorithm.py - Recommendation algorithm
* main.py - Main function that ties all the other sister functions together
* sysdefs.py - System definitions

Packages include:
* spacy (nlp)
* requests (api handling)
* colorama (terminal formatting)

APIs used:
* Open Library (https://openlibrary.org/dev/docs/api/search)
* Google Books API (first-time, in development)


Example run:

1) Would you like your books to be sorted by popularity?(y/n): y
2) What genre are you feeling? (try to be accurate with spelling): automobiles

Top 10 Rated Books:
1. Title: Tax administration
   Author: United States. General Accounting Office
   Rating: 5.0


2. Title: The machine that changed the world
   Author: James P. Womack
   Rating: 5.0


3. Title: Air pollution
   Author: United States. General Accounting Office
   Rating: 5.0


4. Title: How to keep your Volkswagen alive
   Author: Muir, John
   Rating: 5.0


5. Title: So B. It
   Author: Sarah Weeks
   Rating: 4.8333335


6. Title: The One Plus One
   Author: Jojo Moyes, Elizabeth Bower, Ben Elliot, Steven  France, Nicola  Stanton
   Rating: 4.75


7. Title: Fundamentals of automobile body structure design
   Author: Donald E. Malen
   Rating: 4.6666665


8. Title: Fly High, Fly Guy! (Fly Guy)
   Author: Tedd Arnold
   Rating: 4.6666665


9. Title: The Price of Salt
   Author: Patricia Highsmith
   Rating: 4.55


10. Title: Let's go for a drive!
   Author: Mo Willems
   Rating: 4.5454545



Top 5 Most Similar and Rated Books:
1. Title: The machine that changed the world
   Author: James P. Womack
   Rating: 5.0
   Similarity Score: 0.21

2. Title: Let's go for a drive!
   Author: Mo Willems
   Rating: 4.5454545
   Similarity Score: 0.08

3. Title: So B. It
   Author: Sarah Weeks
   Rating: 4.8333335
   Similarity Score: 0.03

4. Title: The Price of Salt
   Author: Patricia Highsmith
   Rating: 4.55
   Similarity Score: -0.03

5. Title: Tax administration
   Author: United States. General Accounting Office
   Rating: 5.0
   Similarity Score: -0.04


#1 Recommended Book for you:
Title: The machine that changed the world
Author: James P. Womack
Rating: 5.0


             Book themes:              

+---------------------------------------++---------------------------------------+
| • Automobile industry and trade | • Automóviles                   |
| • Forecasting                   | • Industria y comercio          |
| • Investigación                 |                                 |
+---------------------------------------++---------------------------------------+
Enter the number of the book for more info (or 'exit' to quit): 1
Book Information:
Title: The machine that changed the world
Author: James P. Womack
Rating: 5.0


             Book themes:              

+---------------------------------------++---------------------------------------+
| • Automobile industry and trade | • Automóviles                   |
| • Forecasting                   | • Industria y comercio          |
| • Investigación                 |                                 |
+---------------------------------------++---------------------------------------+
Enter the number of the book for more info (or 'exit' to quit): 1