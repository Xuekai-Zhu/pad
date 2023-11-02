def solution():
    """Jeannie hikes the 12 miles to Mount Overlook at a pace of 4 miles per hour, and then returns at a pace of 6 miles per hour. How long did her hike take, in hours?"""
    distance = 12
    speed_to = 4
    speed_back = 6
    time_to = distance / speed_to
    time_back = distance / speed_back
    total_time = time_to + time_back
    result = total_time
    return result

print(solution())