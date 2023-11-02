def solution():
    total_cost = 26
    cost_of_drinks = 4 * 2
    cost_of_sandwiches = total_cost - cost_of_drinks
    sandwich_price = cost_of_sandwiches / 3
    result = sandwich_price
    return result

print(solution())