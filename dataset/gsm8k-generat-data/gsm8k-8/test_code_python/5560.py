def solution():
    # Define the height of the tallest tree
    tallest_tree = 108

    # Calculate the height of the middle tree
    middle_tree = 0.5 * tallest_tree - 6

    # Calculate the height of the smallest tree
    smallest_tree = 0.25 * middle_tree

    result = smallest_tree
    return result

print(solution())