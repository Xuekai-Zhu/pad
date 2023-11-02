def solution():
    """A park has three colors of flowering crepe myrtle trees planted: red, white, and pink. When they bloom, a third of them are pink, but only two are red. Most of them are white. There are 42 crepe myrtle trees in the park. How many have white flowers when they bloom?"""
    total_trees = 42
    pink_trees = total_trees / 3
    red_trees = 2
    white_trees = total_trees - pink_trees - red_trees
    result = white_trees
    return result

print(solution())