def solution():
    """In a house, there are 16 cats. Two of them are white, and 25% of them are black. The rest of the cats are grey. How many grey cats are in this house?"""
    # Define the total number of cats
    total_cats = 16

    # Calculate the number of black cats
    black_cats = total_cats * 0.25

    # Calculate the number of white cats
    white_cats = 2

    # Calculate the number of grey cats
    grey_cats = total_cats - black_cats - white_cats

    # return the result
    result = grey_cats
    return result

print(solution())