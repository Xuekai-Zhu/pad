def solution():
    # Calculate how long it takes Peter to read one book
    peter_book_time = 18

    # Calculate how long it takes Kristin to read one book
    kristin_book_time = peter_book_time * 3

    # Calculate how long it takes Kristin to read half of her books
    half_books = 20 / 2
    half_books_time = half_books * kristin_book_time

    result = half_books_time
    return result

print(solution())