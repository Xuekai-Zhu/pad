def solution():
    first_day_distance = 1
    current_distance = first_day_distance
    day = 1

    while current_distance < 10 * first_day_distance:
        day += 1
        current_distance *= 2

    result = day
    return result

print(solution())