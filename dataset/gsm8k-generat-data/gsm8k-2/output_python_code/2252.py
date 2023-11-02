def solution():
    """Ines had $20 in her purse. She bought 3 pounds of peaches, which are $2 per pound at the local farmers’ market. How much did she have left?"""
    starting_amount = 20
    peaches_cost_per_pound = 2
    pounds_of_peaches_bought = 3
    total_cost_of_peaches = peaches_cost_per_pound * pounds_of_peaches_bought
    amount_left = starting_amount - total_cost_of_peaches
    result = amount_left
    return result

print(solution())