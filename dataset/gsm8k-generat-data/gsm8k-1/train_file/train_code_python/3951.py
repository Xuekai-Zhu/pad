def solution():
    """Luis is driving 80 miles in 2 hours. How far will he go in 15 minutes?"""
    distance = 80
    time = 2
    speed = distance / time
    distance_in_quarter_hour = (speed / 60) * 15
    result = distance_in_quarter_hour
    return result

print(solution())