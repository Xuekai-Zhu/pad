def solution():
    """James drives 30 mph for half an hour and then twice as long for twice the speed. How far did he drive in total?"""
    first_leg_time = 0.5
    first_leg_speed = 30
    second_leg_time = 2 * first_leg_time
    second_leg_speed = 2 * first_leg_speed

    # Distance covered in the first leg
    first_leg_distance = first_leg_time * first_leg_speed

    # Distance covered in the second leg
    second_leg_distance = second_leg_time * second_leg_speed

    # Total distance
    total_distance = first_leg_distance + second_leg_distance

    result = total_distance
    return result

print(solution())