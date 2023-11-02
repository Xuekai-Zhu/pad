def solution():
    """John decided to start rowing around a square lake. Each side of the lake is 15 miles. Jake can row at twice the speed he can swim. It takes him 20 minutes to swim 1 mile. How long, in hours, does it take to row the lake?"""
    lake_distance = 15 * 4
    swim_speed = 1 / (20/60) # miles per hour
    row_speed = swim_speed * 2
    row_time = lake_distance / row_speed # hours
    result = row_time
    return result

print(solution())