def solution():
    """Lilly and Fiona are cleaning a room. Between them, it takes 8 hours to clean the room. A quarter of the time spent cleaning was by Lilly and Fiona was responsible for the rest of the cleaning. How long, in minutes, was Fiona cleaning?"""
    total_time = 8 * 60  # converting hours to minutes
    lilly_time = total_time / 4
    fiona_time = total_time - lilly_time
    result = fiona_time
    return result

print(solution())