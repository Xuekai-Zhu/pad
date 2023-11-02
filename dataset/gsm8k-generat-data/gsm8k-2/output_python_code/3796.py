def solution():
    """Ivan had $10 and spent 1/5 of it on cupcakes. He then spent some money on a milkshake and had only $3 left. How much is the milkshake?"""
    initial_amount = 10
    cupcakes_cost = initial_amount / 5
    remaining_amount = initial_amount - cupcakes_cost - 3
    milkshake_cost = remaining_amount
    result = milkshake_cost
    return result

print(solution())