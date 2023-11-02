def solution():
    """A park has three colors of flowering crepe myrtle trees planted: red, white, and pink. When they bloom, a third of them are pink, but only two are red. Most of them are white. There are 42 crepe myrtle trees in the park. How many have white flowers when they bloom?"""
    # Define the number of red and pink trees
    red_trees = 2
    pink_trees = 42 // 3

    # Calculate the number of white trees
    white_trees = 42 - red_trees - pink_trees

    # Return the number of white trees
    result = white_trees
    return result

print(solution())