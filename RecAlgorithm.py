# RecAlgorithm.py - Implement recommendation algorithm

import spacy

def find_most_similar_rated_books(user_input, books, popular_rec_toggle=0, top_n=10):
    nlp = spacy.load("en_core_web_md")
    user_input_embedding = nlp(user_input).vector

    if(popular_rec_toggle):
        # Filter books with # of ratings (popularity)
        sorted_books = [book for book in books if "readinglog_count" in book]

        # Take the top N most-reviewed books
        books = sorted(sorted_books, key=lambda x: x.get("readinglog_count", 0), reverse=True)

    # Filter books with rating avg
    rated_books = [book for book in books if "ratings_average" in book]
    
    # Sort books by ratings in descending order
    sorted_books = sorted(rated_books, key=lambda x: x.get("ratings_average", 0), reverse=True)
    
    # Take the top N rated books
    top_rated_books = sorted_books[:top_n]

    most_similar_rated_books = []

    for book in top_rated_books:
        if "title" in book and "author_name" in book and "subject_key" in book and "subject_facet" in book:
            book_title = book["title"]
            book_embedding = nlp(book_title).vector
            similarity = (
                nlp(" ".join(book["author_name"])).similarity(nlp(user_input)) +
                nlp(" ".join(book["subject_key"])).similarity(nlp(user_input)) +
                nlp(" ".join(book["subject_facet"])).similarity(nlp(user_input)) +
                nlp(book_title).similarity(nlp(user_input))
            )
            most_similar_rated_books.append({"similarity": similarity, "book": book})

    # Sort the most similar books by similarity in descending order
    most_similar_rated_books = sorted(most_similar_rated_books, key=lambda x: x["similarity"], reverse=True)

    return most_similar_rated_books[:5]