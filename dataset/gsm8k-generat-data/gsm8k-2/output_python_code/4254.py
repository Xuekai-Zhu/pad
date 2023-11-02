def solution():
    """Jeannie hikes the 12 miles to Mount Overlook at a pace of 4 miles per hour, and then returns at a pace of 6 miles per hour. How long did her hike take, in hours?"""
    distance = 12
    speed1 = 4
    speed2 = 6
    time1 = distance / speed1
    time2 = distance / speed2
    total_time = time1 + time2
    result = total_time
    return result

print(solution())