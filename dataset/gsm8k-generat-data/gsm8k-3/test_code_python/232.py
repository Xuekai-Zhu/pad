def solution():
    """
    Emery and Serena go to their school library, and each borrows a copy of The life of Jack Steve's book to read for their school project. If Emery can read five times as fast as Serena, and the book takes her 20 days to read, what's the average number of days the two take to read the book?
    """
    # Define Emery's and Serena's reading speeds
    emery_speed = 5
    serena_speed = 1

    # Calculate the time it takes for Emery to read the book
    emery_time = 20 / emery_speed

    # Calculate the time it takes for Serena to read the book
    serena_time = emery_time * emery_speed / serena_speed

    # Calculate the average time it takes for the two to read the book
    avg_time = (emery_time + serena_time) / 2

    # Display the average time
    result = avg_time
    return result

print(solution())