def solution():
    # Calculate the total number of trees and apples
    total_trees = 3 * 4  # John plants a plot of 3 trees by 4 trees
    total_apples = total_trees * 5  # Each tree gives 5 apples

    # Calculate the total amount of money John makes
    total_money = total_apples * 0.5  # He sells each apple for $.5
    result = total_money
    return result

print(solution())