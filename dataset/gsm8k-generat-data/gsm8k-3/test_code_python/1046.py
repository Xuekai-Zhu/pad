def solution():
    """Susan had a bouquet of 3 dozen roses.  She gave half to her daughter, and then placed the rest in a vase.  The next day, one-third of the flowers in the vase were wilted.  After removing the wilted flowers, how many flowers remained in the vase?"""
    
    # Define the number of flowers in a dozen
    FLOWERS_PER_DOZEN = 12
    
    # Define the number of dozens in the bouquet and calculate the total number of flowers
    dozens = 3
    total_flowers = dozens * FLOWERS_PER_DOZEN

    # Calculate the number of flowers given to her daughter
    daughter_flowers = total_flowers / 2

    # Calculate the number of flowers remaining in the vase
    remaining_flowers = total_flowers - daughter_flowers

    # Calculate the number of wilted flowers and subtract them
    wilted_flowers = remaining_flowers / 3
    remaining_flowers = remaining_flowers - wilted_flowers

    # Display the number of remaining flowers
    result = remaining_flowers
    return result

print(solution())