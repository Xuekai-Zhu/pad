def solution():
    """The total distance between 2 towns is 200 miles. Roger and his friend drove 1/4 of the total distance, taking 1 hour to do so. They take lunch for another 1 hour and then drove the remaining distance going at the same speed as before. What's the total amount of time, in hours, Roger and his friend took to travel between the two towns?"""
    total_distance = 200
    distance_traveled = total_distance / 4
    time_spent_traveling = 1
    time_spent_lunching = 1
    speed = distance_traveled / time_spent_traveling
    remaining_distance = total_distance - distance_traveled
    remaining_time = remaining_distance / speed
    total_time = time_spent_traveling + time_spent_lunching + remaining_time
    result = total_time
    return result

print(solution())