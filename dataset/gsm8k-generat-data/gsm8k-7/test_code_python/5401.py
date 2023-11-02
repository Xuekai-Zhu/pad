def solution():
    total_cost = 160
    current_savings = 40
    num_weeks = 8

    # Calculate the remaining amount that Lyka needs to save
    remaining_cost = total_cost - current_savings

    # Calculate the amount Lyka needs to save per week
    savings_per_week = remaining_cost / num_weeks
    result = savings_per_week
    return result

print(solution())