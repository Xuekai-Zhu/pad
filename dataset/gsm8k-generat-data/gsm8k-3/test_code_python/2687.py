def solution():
    """A forester is planting trees. The forest already has 30 native trees. On Monday he triples the number of total trees in the forest by planting new trees. On Tuesday, he plants a third of the amount he planted on Monday. How many trees has the forester planted in total?"""
    # Define the number of original trees and the multiplier
    native_trees = 30
    multiplier = 3

    # Calculate the number of trees planted on Monday
    monday_trees = (native_trees + monday_trees) * multiplier - native_trees

    # Calculate the number of trees planted on Tuesday
    tuesday_trees = monday_trees / 3

    # Calculate the total number of trees planted
    total_trees = native_trees + monday_trees + tuesday_trees

    # Display the total number of trees planted
    result = total_trees
    return result

print(solution())