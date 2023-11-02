def solution():
    
    initial_amount = 10
    cupcakes_cost = initial_amount / 5
    remaining_amount = initial_amount - cupcakes_cost - 3
    milkshake_cost = remaining_amount
    result = milkshake_cost
    return result

print(solution())