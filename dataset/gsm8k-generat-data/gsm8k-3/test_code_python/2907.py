def solution():
    """There are 350 trees in the park, 70% of which are pine trees. How many are not pine trees?"""
    # Define the total number of trees and the percentage of pine trees
    total_trees = 350
    pine_percent = 0.7

    # Calculate the number of pine trees
    pine_trees = total_trees * pine_percent

    # Calculate the number of non-pine trees
    non_pine_trees = total_trees - pine_trees

    # Display the number of non-pine trees
    result = non_pine_trees
    return result

print(solution())