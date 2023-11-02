def solution():
    """Bill is stocking the kitchenware section of the Walmart. He needs to stack 60 pots. On each shelf, he can stack five pots vertically and three sets of vertically stacked pots side-by-side. How many shelves does he need to stock all the pots?"""
    pots_per_shelf = 5 * 3
    shelves_needed = 60 / pots_per_shelf
    result = shelves_needed
    return result

print(solution())