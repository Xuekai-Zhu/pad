def solution():
    """Tod drives his family car 55 miles to the north and 95 miles to the west. If Tod constantly drives 25 miles an hour the entire trip how many hours did Tod drive?"""
    distance_north = 55
    distance_west = 95
    speed = 25
    time_north = distance_north / speed
    time_west = distance_west / speed
    total_time = time_north + time_west
    result = total_time
    return result

print(solution())