def solution():
    """Peter and Kristin are to read 20 fantasy novels each in a week. Peter can read three times as fast as Kristin. If Peter reads one book in 18 hours, how long will Kristin read half of her books?"""
    # Define the number of books and the reading speed of Peter and Kristin
    NUM_BOOKS = 20
    PETER_SPEED = 3 # times faster than Kristin
    PETER_TIME = 18 # hours to read one book

    # Calculate the reading speed of Kristin, relative to Peter
    KRISTIN_SPEED = 1 / PETER_SPEED

    # Calculate Kristin's reading time for half the total number of books
    KRISTIN_TIME = ((NUM_BOOKS / 2) * PETER_TIME) * (1 / PETER_SPEED)

    # Return the result
    result = KRISTIN_TIME
    return result

print(solution())