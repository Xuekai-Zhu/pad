def solution():
    # Number of surfers on the first day
    day_1 = 1500

    # Number of surfers on the second day
    day_2 = day_1 + 600

    # Number of surfers on the third day
    day_3 = (2/5) * day_1

    # Total number of surfers for the three days
    total_surfers = day_1 + day_2 + day_3

    # Average number of surfers for the three days
    average_surfers = total_surfers / 3
    result = average_surfers
    return result

print(solution())