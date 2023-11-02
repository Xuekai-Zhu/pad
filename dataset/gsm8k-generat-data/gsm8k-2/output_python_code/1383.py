def solution():
    """Bill is stocking the kitchenware section of the Walmart. He needs to stack 60 pots. On each shelf, he can stack five pots vertically and three sets of vertically stacked pots side-by-side. How many shelves does he need to stock all the pots?"""
    total_pots = 60
    pots_per_set = 5
    sets_per_shelf = 3
    pots_per_shelf = pots_per_set * sets_per_shelf
    total_shelves = total_pots / pots_per_shelf
    result = total_shelves
    return result

print(solution())