def solution():
    num_blackbirds_per_tree = 3
    num_trees = 7
    num_magpies = 13

    # Calculate the total number of blackbirds in the park
    total_blackbirds = num_blackbirds_per_tree * num_trees

    # Calculate the total number of birds in the park
    total_birds = total_blackbirds + num_magpies
    result = total_birds
    return result

print(solution())