def solution():
    # Initial number of books
    initial_books = 300

    # Books donated by ten people who each donated 5 books
    donated_books = 10 * 5

    # Books borrowed by others to read
    borrowed_books = 140

    # Calculate the total number of books in the store
    total_books = initial_books + donated_books - borrowed_books
    result = total_books
    return result

print(solution())