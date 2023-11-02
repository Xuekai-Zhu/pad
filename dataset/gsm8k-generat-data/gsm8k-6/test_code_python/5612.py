def solution():
    # Calculate the number of books and movies Sue has now
    books_now = 15 - 8 + 9  # Sue returned 8 books and checked out 9 more books
    movies_now = 6 - (1/3) * 6  # Sue returned 1/3 of the movies and kept the remaining 2/3
    result = f"Sue now has {books_now} books and {movies_now} movies"
    return result

print(solution())