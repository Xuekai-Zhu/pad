def solution():
    """Jane bought 2 skirts for $13 each. She also bought 3 blouses for $6 each. She paid the cashier $100. How much change did she receive?"""
    skirt_cost = 13
    blouse_cost = 6
    num_skirts = 2
    num_blouses = 3
    total_cost = (skirt_cost * num_skirts) + (blouse_cost * num_blouses)
    change = 100 - total_cost
    result = change
    return result

print(solution())