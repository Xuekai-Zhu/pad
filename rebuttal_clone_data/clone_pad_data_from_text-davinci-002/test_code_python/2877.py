def solution():
    first_distance = 1500
    first_speed = 75
    first_time = first_distance / first_speed
    second_distance = 750
    second_speed = 25
    second_time = second_distance / second_speed
    if first_time < second_time:
        fastest_time = first_time
    else:
        fastest_time = second_time
    result = fastest_time
    return result

print(solution())