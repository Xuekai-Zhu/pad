def solution():
    tallest_tree = 150  # The tallest tree is 150 feet tall
    middle_tree = (2/3) * tallest_tree  # The middle tree is 2/3 the height of the tallest tree
    shortest_tree = (1/2) * middle_tree  # The shortest tree is half the size of the middle tree
    result = shortest_tree
    return result

print(solution())