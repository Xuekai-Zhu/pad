def solution():
    naps_per_week = 3
    hours_per_nap = 2
    num_days = 70

    # Calculate the total number of naps John takes in 70 days
    total_naps = (naps_per_week * num_days) / 7

    # Calculate the total number of hours John spends napping
    total_hours = total_naps * hours_per_nap
    result = total_hours
    return result

print(solution())