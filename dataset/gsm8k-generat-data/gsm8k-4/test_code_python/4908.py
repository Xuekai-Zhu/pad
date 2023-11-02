def solution():
    """Noah has two closets. Each closet can fit 1/4 as much as Ali's closet, which can fit 200 pairs of jeans. How many jeans can both Noah’s closets fit?"""
    # Calculate the amount of jeans that Ali's closet can fit
    alis_closet = 200

    # Calculate the amount of jeans each of Noah's closet can fit
    noahs_closet = alis_closet * (1 / 4)
    
    # Calculate the total amount of jeans that both of Noah's closet can fit
    total_noahs_closet = noahs_closet * 2

    # return the result
    result = total_noahs_closet
    return result

print(solution())