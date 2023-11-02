def solution():
    starting_sodas = 48
    target_sodas = 6
    weeks = 0

    while starting_sodas > target_sodas:
        starting_sodas /= 2
        weeks += 1

    result = weeks
    return result

print(solution())