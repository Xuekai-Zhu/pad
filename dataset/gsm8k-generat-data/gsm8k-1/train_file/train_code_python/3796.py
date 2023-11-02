def solution():
    """Ivan had $10 and spent 1/5 of it on cupcakes. He then spent some money on a milkshake and had only $3 left. How much is the milkshake?"""
    starting_money = 10
    cupcakes_cost = starting_money / 5
    remaining_money = starting_money - cupcakes_cost - 3
    milkshake_cost = remaining_money
    result = milkshake_cost
    return result

print(solution())