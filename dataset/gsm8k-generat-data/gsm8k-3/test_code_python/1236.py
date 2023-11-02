def solution():
    """In a house, there are 16 cats. Two of them are white, and 25% of them are black. The rest of the cats are grey. How many grey cats are in this house?"""
    # Calculate the number of black cats
    black_cats = int(16 * 0.25)

    # Calculate the number of white cats
    white_cats = 2

    # Calculate the number of grey cats
    grey_cats = 16 - black_cats - white_cats

    # Display the number of grey cats
    result = grey_cats
    return result

print(solution())