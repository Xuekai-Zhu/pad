def solution():
    tallest_tree = 108  # The height of the tallest tree is 108 feet
    middle_tree = tallest_tree / 2 - 6  # The middle tree is 6 feet less than half the height of the tallest tree
    smallest_tree = middle_tree / 4  # The smallest tree is 1/4 the height of the middle tree

    result = smallest_tree
    return result

print(solution())