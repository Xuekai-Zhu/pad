def solution():
    """John decided to start rowing around a square lake. Each side of the lake is 15 miles. Jake can row at twice the speed he can swim. It takes him 20 minutes to swim 1 mile. How long, in hours, does it take to row the lake?"""
    side_length = 15
    distance = side_length * 4
    swim_speed = 1/20 # miles per minute
    row_speed = swim_speed * 2
    travel_time = distance / row_speed # minutes
    travel_time_hours = travel_time / 60 # hours
    result = travel_time_hours
    return result

print(solution())