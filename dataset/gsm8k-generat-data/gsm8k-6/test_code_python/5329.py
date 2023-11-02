def solution():
    # Calculate the number of pink and red crepe myrtle trees in the park
    pink_trees = 42 / 3  # a third of the trees are pink
    red_trees = 2  # only two are red

    # Calculate the number of white crepe myrtle trees in the park
    white_trees = 42 - pink_trees - red_trees  # subtract the number of pink and red trees from the total

    result = white_trees
    return result

print(solution())