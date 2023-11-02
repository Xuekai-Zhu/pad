def solution():
    num_pines = 600  # Given that there are 600 pines
    num_redwoods = 1.2 * num_pines  # The number of redwoods is 20% more than the number of pines

    # Calculate the total number of pines and redwoods
    total_trees = num_pines + num_redwoods
    result = total_trees
    return result

print(solution())