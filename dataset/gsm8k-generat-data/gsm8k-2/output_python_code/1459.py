def solution():
    """A man intends to complete a journey of 24 km in 8 hours. If he travels at a speed of 4km/hr for the first four hours, at what speed does he need to travel for the remainder of the journey to be right on time?"""
    total_distance = 24
    total_time = 8
    first_leg_distance = 4 * 4
    second_leg_distance = total_distance - first_leg_distance
    second_leg_time = total_time - 4
    second_leg_speed = second_leg_distance / second_leg_time
    result = second_leg_speed
    return result

print(solution())