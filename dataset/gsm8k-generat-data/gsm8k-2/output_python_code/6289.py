def solution():
    """There are three trees in the town square. The tallest tree is 150 feet tall. The middle height tree is 2/3 the height of the tallest tree. The shortest tree is half the size of the middle tree. How tall is the shortest tree?"""
    tallest_tree = 150
    middle_tree = 2/3 * tallest_tree
    shortest_tree = 1/2 * middle_tree
    result = shortest_tree
    return result

print(solution())