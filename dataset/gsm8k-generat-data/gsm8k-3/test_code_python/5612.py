def solution():
    """Sue borrowed 15 books and 6 movies. She returned 8 books. She then returned a third of the movies to the library and checked out 9 more books. How many movies and books does Sue now have?"""
    # Define the initial number of books and movies borrowed
    books = 15
    movies = 6

    # Return 8 books
    books -= 8

    # Return a third of the movies and update the movie count
    movies = movies - (movies // 3)

    # Check out 9 more books and update the book count
    books += 9

    # Display the new counts of books and movies
    result = (books, movies)
    return result

print(solution())