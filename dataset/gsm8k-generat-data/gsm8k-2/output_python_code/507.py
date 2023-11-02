def solution():
    """James drives 30 mph for half an hour and then twice as long for twice the speed. How far did he drive in total?"""
    first_distance = 30 * 0.5
    second_time = 1.5
    second_speed = 2 * 30
    second_distance = second_time * second_speed
    total_distance = first_distance + second_distance
    result = total_distance
    return result

print(solution())