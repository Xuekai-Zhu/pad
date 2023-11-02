def solution():
    cost_per_cup = 2
    total_cost = 20
    desired_profit = 80
    break_even = total_cost / cost_per_cup
    cups_needed = desired_profit / cost_per_cup + break_even
    result = cups_needed
    return result

print(solution())