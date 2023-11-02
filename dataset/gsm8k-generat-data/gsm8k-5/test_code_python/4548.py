def solution():
    brother_time = 8   # John's brother takes 8 hours to read a book
    john_speed = 1.6   # John reads 60% faster than his brother (1 + 0.6 = 1.6)
    num_books = 3      # John wants to read 3 books

    # Calculate John's reading time for one book
    john_time_one_book = brother_time / john_speed

    # Calculate John's reading time for three books
    john_time_three_books = john_time_one_book * num_books
    result = john_time_three_books
    return result

print(solution())