def solution():
    """Lilly and Fiona are cleaning a room. Between them, it takes 8 hours to clean the room. A quarter of the time spent cleaning was by Lilly and Fiona was responsible for the rest of the cleaning. How long, in minutes, was Fiona cleaning?"""
    total_time_in_minutes = 8*60
    lilly_time_in_minutes = total_time_in_minutes / 4
    fiona_time_in_minutes = total_time_in_minutes - lilly_time_in_minutes
    result = fiona_time_in_minutes
    return result

print(solution())