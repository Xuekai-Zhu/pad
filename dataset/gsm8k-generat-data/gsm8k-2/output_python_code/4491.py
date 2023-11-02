def solution():
    """Jane bought 2 skirts for $13 each. She also bought 3 blouses for $6 each. She paid the cashier $100. How much change did she receive?"""
    skirt_price = 13
    blouse_price = 6
    total_skirt_cost = 2 * skirt_price
    total_blouse_cost = 3 * blouse_price
    total_cost = total_skirt_cost + total_blouse_cost
    change = 100 - total_cost
    result = change
    return result

print(solution())