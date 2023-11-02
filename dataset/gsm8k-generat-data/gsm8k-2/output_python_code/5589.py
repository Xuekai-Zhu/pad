def solution():
    """A desert has 3/5 fewer palm trees than a nearby forest, which has 5000 palm trees. How many palm trees are there in both the desert and the forest combined?"""
    forest_trees = 5000
    desert_trees = forest_trees - (3/5 * forest_trees)
    total_trees = forest_trees + desert_trees
    result = total_trees
    return result

print(solution())