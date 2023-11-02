def solution():
    # Calculate the number of patients seen in a day
    patients_per_day = 8 / 0.5
    # Calculate the number of toothbrushes given to each patient
    toothbrushes_per_patient = 2
    # Calculate the total toothbrushes given in a day
    toothbrushes_per_day = patients_per_day * toothbrushes_per_patient
    # Calculate the total toothbrushes given in a week
    toothbrushes_per_week = toothbrushes_per_day * 5
    result = toothbrushes_per_week
    return result

print(solution())