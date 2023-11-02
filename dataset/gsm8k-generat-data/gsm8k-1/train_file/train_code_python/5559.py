def solution():
    """The tallest of 3 trees is 108 feet. The middle sized tree is 6 feet less than half the height of the tallest tree. The smallest tree is 1/4 the height of the middle tree. How tall is the smallest tree?"""
    tallest_tree = 108
    middle_tree = (tallest_tree / 2) - 6
    smallest_tree = middle_tree / 4
    result = smallest_tree
    return result

print(solution())