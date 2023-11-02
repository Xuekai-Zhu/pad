def solution():
    """John can read a book 60% faster than his brother.  If his brother takes 8 hours to read a book, how long would it take John to read 3 books?"""
    # Define brother's reading speed and time per book
    brother_speed = 1 / 8 # 1 book in 8 hours
    brother_time_per_book = 8

    # Calculate John's reading speed and time per book
    john_speed = brother_speed * 1.6 # 60% faster
    john_time_per_book = 1 / john_speed

    # Calculate John's total reading time for 3 books
    total_time = john_time_per_book * 3

    # Display John's total reading time
    result = total_time
    return result

print(solution())