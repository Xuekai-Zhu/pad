def solution():
    """Bill is stocking the kitchenware section of the Walmart. He needs to stack 60 pots. On each shelf, he can stack five pots vertically and three sets of vertically stacked pots side-by-side. How many shelves does he need to stock all the pots?"""
    # Define the number of pots to stack
    pots_to_stack = 60

    # Calculate the total number of sets of vertically stacked pots
    vertical_sets = pots_to_stack // 5

    # Calculate the total number of shelves
    shelves = vertical_sets // 3

    # If there are any remaining sets of vertically stacked pots, add an additional shelf
    if vertical_sets % 3 != 0:
        shelves += 1
    
    result = shelves
    return result

print(solution())