def solution():
    total_trees = 42  # There are 42 crepe myrtle trees in the park
    pink_trees = total_trees / 3  # A third of the trees are pink
    red_trees = 2  # Only two trees are red
    white_trees = total_trees - pink_trees - red_trees  # The rest of the trees are white

    result = white_trees
    return result

print(solution())