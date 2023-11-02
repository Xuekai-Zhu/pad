def solution():
    """John plants a plot of 3 trees by 4 trees. Each tree gives 5 apples. He sells each apple for $.5. How much money does he make, in dollars?"""
    # Define the number of trees and the number of apples per tree
    NUM_TREES = 3 * 4
    APPLES_PER_TREE = 5

    # Calculate the total number of apples
    total_apples = NUM_TREES * APPLES_PER_TREE

    # Calculate the total earnings from selling apples
    earnings = total_apples * 0.5

    # return the result
    result = earnings
    return result

print(solution())