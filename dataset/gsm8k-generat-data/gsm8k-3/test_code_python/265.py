def solution():
    """John plants a plot of 3 trees by 4 trees.  Each tree gives 5 apples.  He sells each apple for $.5.  How much money does he make, in dollars?"""
    # Calculate the total number of trees and apples
    total_trees = 3 * 4
    total_apples = total_trees * 5

    # Calculate the total amount of money John makes
    total_money = total_apples * 0.5

    # Display the total amount of money John makes
    result = total_money
    return result

print(solution())