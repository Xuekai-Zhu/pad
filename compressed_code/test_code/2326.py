def solution():
    
    num_sandwiches = 3
    num_drinks = 2
    total_cost = 26
    drinks_cost = num_drinks * 4
    sandwich_cost = (total_cost - drinks_cost) / num_sandwiches
    result = sandwich_cost
    return result

print(solution())