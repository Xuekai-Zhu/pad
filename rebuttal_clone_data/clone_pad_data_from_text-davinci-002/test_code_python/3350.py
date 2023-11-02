def solution():
    sodas_per_week = 48
    reduction_per_week = sodas_per_week / 2
    target_sodas_per_week = 6
    weeks = (sodas_per_week - target_sodas_per_week) / reduction_per_week
    result = weeks
    return result

print(solution())