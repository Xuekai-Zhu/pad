def solution():
    total_cost = 90  # Cost of the new sneakers
    initial_savings = 15  # Amount already saved by Lee
    remaining_cost = total_cost - initial_savings  # Amount Lee needs to make from selling old action figures
    remaining_cost_with_margin = remaining_cost + 25  # Amount Lee can spend on action figures with $25 left over

    # Calculate the cost per action figure
    cost_per_figure = remaining_cost_with_margin / 10
    result = cost_per_figure
    return result

print(solution())