def solution():
    
    num_sandwiches = 3
    num_drinks = 2
    total_spent = 26
    drink_cost = 4
    sandwich_cost = (total_spent - (num_drinks * drink_cost)) / num_sandwiches
    result = sandwich_cost
    return result

print(solution())