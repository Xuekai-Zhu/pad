def solution():
    """Ahmed has 8 orange trees and four times as many apple trees in his orchard as Hassan. If Hassan has one apple tree and two orange trees, and they both have only apple and orange trees in their orchards, how many more trees are in Ahmed's orchard than in Hassan's?"""
    # Define the number of apple trees Hassan has
    HASSAN_APPLE_TREES = 1

    # Define the number of orange trees Hassan has
    HASSAN_ORANGE_TREES = 2

    # Calculate the number of apple trees Ahmed has
    AHMED_APPLE_TREES = HASSAN_APPLE_TREES * 4

    # Calculate the number of orange trees Ahmed has
    AHMED_ORANGE_TREES = 8

    # Calculate the total number of trees Ahmed has
    AHMED_TOTAL_TREES = AHMED_APPLE_TREES + AHMED_ORANGE_TREES

    # Calculate the total number of trees Hassan has
    HASSAN_TOTAL_TREES = HASSAN_APPLE_TREES + HASSAN_ORANGE_TREES

    # Calculate the difference in the total number of trees between Ahmed and Hassan
    DIFFERENCE = AHMED_TOTAL_TREES - HASSAN_TOTAL_TREES

    # Display the difference in the total number of trees between Ahmed and Hassan
    result = DIFFERENCE
    return result

print(solution())