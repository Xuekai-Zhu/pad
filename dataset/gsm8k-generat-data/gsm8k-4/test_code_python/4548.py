def solution():
    """John can read a book 60% faster than his brother. If his brother takes 8 hours to read a book, how long would it take John to read 3 books?"""
    # Define the reading speed ratio between John and his brother
    reading_speed_ratio = 1.6

    # Calculate the reading time for John's brother
    brother_reading_time = 8

    # Calculate the reading time for John
    john_reading_time = brother_reading_time / reading_speed_ratio

    # Calculate the total reading time for John to read 3 books
    total_reading_time = john_reading_time * 3

    # return the result
    result = total_reading_time
    return result

print(solution())