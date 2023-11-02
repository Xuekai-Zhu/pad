def solution():
    # Calculate how long it takes John's brother to read one book
    brother_time_per_book = 8

    # Calculate John's reading speed compared to his brother's
    john_speed_ratio = 1 + 0.6
    # John is able to read 1.6 times as fast as his brother

    # Calculate how long it takes John to read one book
    john_time_per_book = brother_time_per_book / john_speed_ratio

    # Calculate how long it takes John to read three books
    john_total_time = 3 * john_time_per_book
    result = john_total_time
    return result

print(solution())