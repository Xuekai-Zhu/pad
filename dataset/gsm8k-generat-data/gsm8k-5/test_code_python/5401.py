def solution():
    total_cost = 160  # The total cost of the smartphone is $160
    initial_savings = 40  # Lyka has $40 initial savings
    time_in_weeks = 8  # Two months is equivalent to 8 weeks

    # Calculate the remaining amount Lyka needs to save for
    remaining_cost = total_cost - initial_savings

    # Calculate the amount Lyka needs to save per week
    amount_per_week = remaining_cost / time_in_weeks
    result = amount_per_week
    return result

print(solution())