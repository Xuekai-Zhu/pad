def solution():
    """Faith went to a baking shop and bought flour that cost $5 and a cake stand that costs $28. She then gave the cashier two $20 bills and $3 in loose coins. How much change will she receive?"""
    flour_cost = 5
    cake_stand_cost = 28
    total_cost = flour_cost + cake_stand_cost
    payment = (2 * 20) + 3
    change = payment - total_cost
    result = change
    return result

print(solution())