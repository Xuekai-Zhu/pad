def solution():
    """Sue borrowed 15 books and 6 movies. She returned 8 books. She then returned a third of the movies to the library and checked out 9 more books. How many movies and books does Sue now have?"""
    borrowed_books = 15
    borrowed_movies = 6
    returned_books = 8
    returned_movies = borrowed_movies / 3
    remaining_books = borrowed_books - returned_books + 9
    remaining_movies = borrowed_movies - returned_movies
    result = {"books": remaining_books, "movies": remaining_movies}
    return result

print(solution())