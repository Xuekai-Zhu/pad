def solution():
    num_pines = 600
    redwoods_ratio = 1.20  # 20% more than pines

    # Calculate the number of redwoods
    num_redwoods = num_pines * redwoods_ratio

    # Calculate the total number of trees in the national park
    total_trees = num_pines + num_redwoods
    result = total_trees
    return result

print(solution())