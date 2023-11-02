def solution():
    """If a vehicle is driven 12 miles on Monday, 18 miles on Tuesday, and 21 miles on Wednesday. What is the average distance traveled per day?"""
    distance_monday = 12
    distance_tuesday = 18
    distance_wednesday = 21
    days = 3
    total_distance = distance_monday + distance_tuesday + distance_wednesday
    average_distance = total_distance / days
    result = average_distance
    return result

print(solution())