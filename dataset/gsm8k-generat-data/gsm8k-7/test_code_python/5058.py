def solution():
    num_trees_4th = 30
    num_trees_5th = num_trees_4th * 2
    num_trees_6th = (num_trees_5th * 3) - 30
    total_num_trees = num_trees_4th + num_trees_5th + num_trees_6th
    result = total_num_trees
    return result

print(solution())