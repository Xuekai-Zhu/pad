def solution():
    """Peter and Kristin are to read 20 fantasy novels each in a week. Peter can read three times as fast as Kristin. If Peter reads one book in 18 hours, how long will Kristin read half of her books?"""
    # Define the number of books to be read and Peter's reading speed
    num_books = 20
    peter_speed = 1 / 18 # in books per hour

    # Calculate Kristin's reading speed
    kristin_speed = peter_speed / 3

    # Calculate the time it will take Peter to read all the books
    peter_time = num_books / peter_speed

    # Calculate the number of books Kristin needs to read
    kristin_books = num_books / 2

    # Calculate the time it will take Kristin to read half of her books
    kristin_time = kristin_books / kristin_speed

    # Display the time it will take Kristin to read half of her books
    result = kristin_time
    return result

print(solution())