def solution():
    marathon_distance = 26.3
    starting_distance = 3
    months = 1

    while starting_distance < marathon_distance:
        starting_distance *= 2
        months += 1

    result = months
    return result

print(solution())