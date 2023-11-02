def solution():
    """Randy has 60 mango trees on his farm. He also has 5 less than half as many coconut trees as mango trees. How many trees does Randy have in all on his farm?"""
    mango_trees = 60
    coconut_trees = (mango_trees / 2) - 5
    total_trees = mango_trees + coconut_trees
    result = total_trees
    return result

print(solution())