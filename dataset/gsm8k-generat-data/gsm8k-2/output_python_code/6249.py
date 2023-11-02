def solution():
    """Bob drove for one and a half hours at 60/mph. He then hit construction and drove for 2 hours at 45/mph. How many miles did Bob travel in those 3 and a half hours?"""
    first_leg_time = 1.5
    first_leg_speed = 60
    first_leg_distance = first_leg_time * first_leg_speed
    second_leg_time = 2
    second_leg_speed = 45
    second_leg_distance = second_leg_time * second_leg_speed
    total_distance = first_leg_distance + second_leg_distance
    result = total_distance
    return result

print(solution())