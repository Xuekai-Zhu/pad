def solution():
    """The tallest of 3 trees is 108 feet. The middle sized tree is 6 feet less than half the height of the tallest tree. The smallest tree is 1/4 the height of the middle tree. How tall is the smallest tree?"""
    tallest_tree_height = 108
    middle_tree_height = (0.5 * tallest_tree_height) - 6
    smallest_tree_height = 0.25 * middle_tree_height
    result = smallest_tree_height
    return result

print(solution())