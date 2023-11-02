def solution():
    toothbrush_per_patient = 2
    hours_per_visit = 0.5
    hours_per_day = 8
    patients_per_day = hours_per_day / hours_per_visit
    days_per_week = 5

    # Calculate the total number of toothbrushes given away in a week
    total_toothbrushes = toothbrush_per_patient * patients_per_day * days_per_week
    result = total_toothbrushes
    return result

print(solution())