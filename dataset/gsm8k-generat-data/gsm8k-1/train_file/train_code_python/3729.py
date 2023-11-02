def solution():
    """Peter and Kristin are to read 20 fantasy novels each in a week. Peter can read three times as fast as Kristin. If Peter reads one book in 18 hours, how long will Kristin read half of her books?"""
    peter_speed = 1 / 18  # Peter can read one book in 18 hours
    kristin_speed = peter_speed / 3  # Peter reads three times as fast as Kristin
    kristin_books = 20  # Kristin has to read 20 fantasy novels in a week
    kristin_books_to_read = kristin_books / 2  # Kristin has to read half of her books
    time_taken = kristin_books_to_read / kristin_speed  # Time taken for Kristin to read half of her books
    result = time_taken
    return result

print(solution())