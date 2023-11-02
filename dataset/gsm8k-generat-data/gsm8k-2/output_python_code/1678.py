def solution():
    """A park is 1000 feet long and 2000 feet wide. If there is 1 tree per 20 square feet, how many trees are there in the park?"""
    park_area = 1000 * 2000
    tree_density = 1 / 20
    total_trees = park_area * tree_density
    result = total_trees
    return result

print(solution())