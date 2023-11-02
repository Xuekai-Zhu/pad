def solution():
    """There are three trees in Eddy's backyard. The shortest tree has a height of 6 feet, and the second tree has a height of 5 feet more than the shortest tree. The height of the tallest tree is twice the height of the two trees combined. How tall is the tallest tree?"""
    shortest_tree = 6
    second_tree = shortest_tree + 5
    combined_height = shortest_tree + second_tree
    tallest_tree = combined_height * 2
    result = tallest_tree
    return result

print(solution())