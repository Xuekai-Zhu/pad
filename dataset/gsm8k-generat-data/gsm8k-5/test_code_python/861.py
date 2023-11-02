def solution():
    toothbrushes_per_patient = 2  # The dental office gives away 2 toothbrushes per patient
    time_per_visit = 0.5  # Each patient visit takes 0.5 hours
    hours_per_day = 8  # The dental office works 8-hour days
    days_per_week = 5  # The dental office works 5 days per week

    # Calculate the total number of patient visits in a week
    total_visits = hours_per_day * days_per_week / time_per_visit

    # Calculate the total number of toothbrushes given away in a week
    total_toothbrushes = total_visits * toothbrushes_per_patient
    result = total_toothbrushes
    return result

print(solution())