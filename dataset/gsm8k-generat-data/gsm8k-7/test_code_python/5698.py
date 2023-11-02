def solution():
    current_savings = 20
    weekly_savings = 10
    vacuum_cost = 120

    # Calculate how much more Daria needs to save
    remaining_cost = vacuum_cost - current_savings

    # Calculate the number of weeks it will take Daria to save enough money
    num_weeks = remaining_cost / weekly_savings
    result = num_weeks
    return result

print(solution())