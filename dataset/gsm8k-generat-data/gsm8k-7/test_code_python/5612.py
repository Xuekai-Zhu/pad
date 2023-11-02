def solution():
    borrowed_books = 15
    borrowed_movies = 6
    returned_books = 8
    returned_movies = borrowed_movies / 3
    checked_out_books = 9

    # Calculate the total number of books that Sue has now
    total_books = borrowed_books - returned_books + checked_out_books

    # Calculate the total number of movies that Sue has now
    total_movies = borrowed_movies - returned_movies
    result = (total_books, total_movies)
    return result

print(solution())