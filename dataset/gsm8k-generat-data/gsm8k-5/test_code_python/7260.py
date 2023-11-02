def solution():
    birds_per_tree = 3  # There are 3 blackbirds in each tree
    number_of_trees = 7  # There are 7 trees in the park
    total_blackbirds = birds_per_tree * number_of_trees  # Total number of blackbirds in the park
    magpies = 13  # There are 13 magpies in the park

    # Calculate the total number of birds in the park
    total_birds = total_blackbirds + magpies
    result = total_birds
    return result

print(solution())