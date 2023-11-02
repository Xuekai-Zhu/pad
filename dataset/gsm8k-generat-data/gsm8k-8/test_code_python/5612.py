def solution():
    # Define the initial number of books and movies
    num_books = 15
    num_movies = 6

    # Return 8 books
    num_books -= 8

    # Return a third of movies
    num_movies -= num_movies // 3

    # Check out 9 more books
    num_books += 9

    # Calculate total number of books and movies
    total = num_books + num_movies

    # Return a tuple with the number of books and movies
    result = (num_books, num_movies)
    return result

print(solution())