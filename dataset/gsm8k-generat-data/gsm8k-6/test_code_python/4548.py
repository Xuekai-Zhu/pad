def solution():
    brother_time = 8  # hours it takes John's brother to read a book
    john_speed = 1 + 0.6  # John reads 60% faster than his brother
    john_time = brother_time / john_speed  # time it takes John to read one book
    john_time_three_books = john_time * 3  # time it takes John to read three books
    result = john_time_three_books
    return result

print(solution())