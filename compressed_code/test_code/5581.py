def solution():
    
    starting_balance = 40
    pizza_cost = 2.75
    soda_cost = 1.5
    jeans_cost = 11.5
    total_spent = pizza_cost + soda_cost + jeans_cost
    remaining_balance = starting_balance - total_spent
    quarters = remaining_balance * 4 / 1
    result = quarters
    return result

print(solution())