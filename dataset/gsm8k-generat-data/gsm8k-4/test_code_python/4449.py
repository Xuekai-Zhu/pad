def solution():
    """Ahmed has 8 orange trees and four times as many apple trees in his orchard as Hassan. If Hassan has one apple tree and two orange trees, and they both have only apple and orange trees in their orchards, how many more trees are in Ahmed's orchard than in Hassan's?"""
    # Define the number of orange trees Ahmed has
    ahmed_orange = 8

    # Define the ratio of apple trees to orange trees Hassan has
    hassan_ratio = 4

    # Define the number of apple trees Hassan has based on the given ratio
    hassan_apple = hassan_ratio * 1
    # Define the number of orange trees Hassan has based on the given ratio
    hassan_orange = hassan_ratio * 2

    # Calculate the total number of trees in Ahmed's orchard
    ahmed_total = ahmed_orange + (hassan_apple * 4) + (hassan_orange * 4)

    # Calculate the total number of trees in Hassan's orchard
    hassan_total = hassan_apple + hassan_orange

    # Calculate the difference in number of trees between the two orchards
    diff = ahmed_total - hassan_total

    # Return the result
    result = diff
    return result

print(solution())