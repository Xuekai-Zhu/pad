def solution():
    # Calculate the number of seeds James collected from both trees
    num_seeds_total = 20 * 2 * 20  # 2 trees, with 20 plants each, with 1 seed per plant

    # Calculate the number of seeds James chose to plant
    num_seeds_planted = 0.6 * num_seeds_total  # 60% of the seeds collected

    # Calculate the number of trees James planted
    num_trees_planted = num_seeds_planted / 20  # 1 tree needs 20 seeds to plant

    result = num_trees_planted
    return result

print(solution())