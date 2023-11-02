def solution():
    num_times_per_day = 40
    crab_meat_per_time = 1.5
    price_per_pound = 8
    num_days_per_week = 7
    num_closed_days_per_week = 3

    # Calculate the total number of times Johnny makes the crab dish per week
    num_times_per_week = num_times_per_day * (num_days_per_week - num_closed_days_per_week)

    # Calculate the total amount of crab meat used per week
    total_crab_meat_per_week = num_times_per_week * crab_meat_per_time

    # Calculate the total cost of crab meat per week
    total_cost_per_week = total_crab_meat_per_week * price_per_pound
    result = total_cost_per_week
    return result

print(solution())