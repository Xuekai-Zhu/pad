def solution():
    num_beignets_per_day = 3
    num_weeks = 16

    # Calculate the total number of days in 16 weeks
    total_days = num_weeks * 7

    # Calculate the total number of beignets Sandra will eat
    total_beignets = num_beignets_per_day * total_days

    result = total_beignets
    return result

print(solution())