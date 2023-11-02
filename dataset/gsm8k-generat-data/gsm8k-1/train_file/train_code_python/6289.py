def solution():
    """There are three trees in the town square. The tallest tree is 150 feet tall. The middle height tree is 2/3 the height of the tallest tree. The shortest tree is half the size of the middle tree. How tall is the shortest tree?"""
    tallest_tree_height = 150
    middle_tree_height = tallest_tree_height * (2/3)
    shortest_tree_height = middle_tree_height / 2
    result = shortest_tree_height
    return result

print(solution())