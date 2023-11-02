def solution():
    current_distance = 1
    day_count = 1

    while current_distance <= 10:
        current_distance *= 2
        day_count += 1

    result = day_count
    return result

print(solution())