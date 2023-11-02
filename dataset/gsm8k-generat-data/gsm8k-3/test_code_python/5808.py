def solution():
    """Lilly and Fiona are cleaning a room. Between them, it takes 8 hours to clean the room. A quarter of the time spent cleaning was by Lilly and Fiona was responsible for the rest of the cleaning. How long, in minutes, was Fiona cleaning?"""
    # Calculate total time in minutes
    total_time = 8 * 60

    # Calculate Lilly's time in minutes
    lilly_time = total_time / 4

    # Calculate Fiona's time in minutes
    fiona_time = total_time - lilly_time

    # Display Fiona's time in minutes
    result = fiona_time
    return result

print(solution())