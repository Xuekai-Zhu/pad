def solution():
    """Emery and Serena go to their school library, and each borrows a copy of The life of Jack Steve's book to read for their school project. If Emery can read five times as fast as Serena, and the book takes her 20 days to read, what's the average number of days the two take to read the book?"""
    # Define the number of days it takes Serena to read the book
    serena_days = 20

    # Calculate the number of days it takes Emery to read the book
    emery_days = serena_days / 5

    # Calculate the total number of days to read the book together
    total_days = serena_days + emery_days

    # Calculate the average number of days to read the book
    average_days = total_days / 2

    result = average_days
    return result

print(solution())