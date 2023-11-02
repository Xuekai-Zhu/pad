def solution():
    """John goes to the market with €100. He buys a roast for €17 and vegetables for €11. How much money does he have left?"""
    initial_money = 100
    roast_cost = 17
    veggie_cost = 11
    remaining_money = initial_money - (roast_cost + veggie_cost)
    result = remaining_money
    return result

print(solution())