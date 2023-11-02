def solution():
    """Susan had a bouquet of 3 dozen roses. She gave half to her daughter, and then placed the rest in a vase. The next day, one-third of the flowers in the vase were wilted. After removing the wilted flowers, how many flowers remained in the vase?"""
    
    # Define the number of roses in a dozen and the total number of roses
    ROSES_PER_DOZEN = 12
    total_roses = 3 * ROSES_PER_DOZEN

    # Calculate the number of roses given to her daughter
    daughter_roses = total_roses / 2

    # Calculate the number of roses remaining in the vase
    vase_roses = total_roses - daughter_roses

    # Calculate the number of wilted roses
    wilted_roses = vase_roses / 3

    # Remove the wilted roses from the vase
    remaining_roses = vase_roses - wilted_roses

    result = remaining_roses
    return result

print(solution())