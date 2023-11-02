def solution():
    pen_cost = 30  # The pen costs $30
    kate_budget = pen_cost / 3  # Kate only has money for a third of the pen's cost
    money_needed = pen_cost - kate_budget  # Calculate how much more money Kate needs to buy the pen

    result = money_needed
    return result

print(solution())