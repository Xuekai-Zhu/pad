def solution():
    patients_per_day = 8 * 2  # 16 patients per day
    visits_per_day = patients_per_day / 0.5  # 32 visits per day
    toothbrushes_per_day = patients_per_day * 2  # 32 toothbrushes per day
    toothbrushes_per_week = toothbrushes_per_day * 5  # 160 toothbrushes per week
    result = toothbrushes_per_week
    return result

print(solution())