def solution():
    """Lilly and Fiona are cleaning a room. Between them, it takes 8 hours to clean the room. A quarter of the time spent cleaning was by Lilly and Fiona was responsible for the rest of the cleaning. How long, in minutes, was Fiona cleaning?"""
    # Define the total time it takes both of them to clean the room
    total_time = 8

    # Calculate the time Lilly spent cleaning (1/4 of the total time)
    lilly_time = total_time / 4

    # Calculate the time Fiona spent cleaning (the rest of the total time)
    fiona_time = total_time - lilly_time

    # Convert Fiona's cleaning time to minutes
    fiona_time_minutes = fiona_time * 60

    # Return the result
    result = fiona_time_minutes
    return result

print(solution())