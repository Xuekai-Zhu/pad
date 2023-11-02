def solution():
    """Sue borrowed 15 books and 6 movies. She returned 8 books. She then returned a third of the movies to the library and checked out 9 more books. How many movies and books does Sue now have?"""
    # Define the initial number of books and movies
    initial_books = 15
    initial_movies = 6

    # Update the number of books and movies after returning some
    remaining_books = initial_books - 8
    returned_movies = initial_movies // 3
    remaining_movies = initial_movies - returned_movies

    # Check out more books
    new_books = 9
    total_books = remaining_books + new_books

    # Calculate the final number of books and movies
    final_books = total_books
    final_movies = remaining_movies

    # Return the result as a tuple
    result = (final_books, final_movies)
    return result

print(solution())