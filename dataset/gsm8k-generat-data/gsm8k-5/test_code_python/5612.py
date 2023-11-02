def solution():
    # Initial count of books and movies
    books = 15
    movies = 6

    # Returning 8 books
    books -= 8

    # Returning a third of the movies
    movies -= (1/3) * 6

    # Checking out 9 more books
    books += 9

    # Total count of books and movies
    total_books = books
    total_movies = movies

    result = (total_books, total_movies)
    return result

print(solution())