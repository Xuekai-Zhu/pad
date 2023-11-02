def solution():
    """A forester is planting trees. The forest already has 30 native trees. On Monday he triples the number of total trees in the forest by planting new trees. On Tuesday, he plants a third of the amount he planted on Monday. How many trees has the forester planted in total?"""
    native_trees = 30
    monday_ratio = 3
    tuesday_ratio = 1 / 3
    total_ratio = monday_ratio + tuesday_ratio
    planted_trees = native_trees * total_ratio
    result = planted_trees
    return result

print(solution())