def solution():
    """A developer was buying land. He bought 4 acres at $1,863 per acre. He then split the land he purchased into 9 lots. How much should he sell each lot for just to break even?"""
    acres_bought = 4
    cost_per_acre = 1863
    total_cost = acres_bought * cost_per_acre
    lots = 9
    break_even_price = total_cost / lots
    result = break_even_price
    return result

print(solution())