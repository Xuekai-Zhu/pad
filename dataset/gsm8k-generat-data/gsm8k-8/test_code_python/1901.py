def solution():
    total_distance = 200
    initial_distance = total_distance / 4
    remaining_distance = total_distance - initial_distance
    time_for_first_leg = 1
    time_for_lunch = 1
    speed = initial_distance / time_for_first_leg
    time_for_second_leg = remaining_distance / speed

    total_time = time_for_first_leg + time_for_lunch + time_for_second_leg
    result = total_time
    return result

print(solution())