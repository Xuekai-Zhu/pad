def solution():
    # Define the number of pines in the national park
    num_pines = 600

    # Calculate the number of redwoods, which is 20% more than the number of pines
    num_redwoods = num_pines * 1.2

    # Calculate the total number of pines and redwoods
    total_trees = num_pines + num_redwoods

    result = total_trees
    return result

print(solution())