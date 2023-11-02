def solution():
    sodas_per_week = 48
    target_sodas_per_week = 6
    weeks = 0

    while sodas_per_week > target_sodas_per_week:
        sodas_per_week /= 2
        weeks += 1

    result = weeks
    return result

print(solution())