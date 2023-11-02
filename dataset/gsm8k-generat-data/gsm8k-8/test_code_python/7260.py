def solution():
    # Calculate the number of blackbirds in the park
    blackbirds_per_tree = 3
    total_trees = 7
    total_blackbirds = blackbirds_per_tree * total_trees

    # Add the number of magpies in the park to get the total number of birds
    total_birds = total_blackbirds + 13
    result = total_birds
    return result

print(solution())