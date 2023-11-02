def solution():
    """The tallest of 3 trees is 108 feet.  The middle sized tree is 6 feet less than half the height of the tallest tree. The smallest tree is 1/4 the height of the middle tree.  How tall is the smallest tree?"""
    # Define the height of the tallest tree
    tallest_tree = 108

    # Calculate the height of the middle tree
    middle_tree = (tallest_tree / 2) - 6

    # Calculate the height of the smallest tree
    smallest_tree = middle_tree / 4

    # Display the height of the smallest tree
    result = smallest_tree
    return result

print(solution())