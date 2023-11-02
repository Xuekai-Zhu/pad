def solution():
    """The total distance between 2 towns is 200 miles. Roger and his friend drove 1/4 of the total distance, taking 1 hour to do so. They take lunch for another 1 hour and then drove the remaining distance going at the same speed as before. What's the total amount of time, in hours, Roger and his friend took to travel between the two towns?"""
    total_distance = 200
    first_leg_distance = total_distance / 4
    first_leg_time = 1
    lunch_time = 1
    second_leg_distance = total_distance - first_leg_distance
    second_leg_time = (second_leg_distance / first_leg_distance) * first_leg_time
    total_time = first_leg_time + lunch_time + second_leg_time
    result = total_time
    return result

print(solution())