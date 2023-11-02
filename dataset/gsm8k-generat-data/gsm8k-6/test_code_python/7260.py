def solution():
    # Calculate the total number of blackbirds in the park
    blackbirds_in_tree = 3  # number of blackbirds in each tree
    trees_in_park = 7  # number of trees in the park
    total_blackbirds = blackbirds_in_tree * trees_in_park

    # Add the number of magpies to get the total number of birds
    magpies = 13
    total_birds = total_blackbirds + magpies
    result = total_birds
    return result

print(solution())