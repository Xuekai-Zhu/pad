def solution():
    """In a national park, the number of redwoods is 20% more than the number of pines. If there are 600 pines in the national park, calculate the total number of pines and redwoods that are there."""
    # Define the percentage increase of redwoods compared to pines
    redwood_increase = 0.2

    # Calculate the number of redwoods
    redwood_count = 600 * (1 + redwood_increase)

    # Calculate the total number of trees
    total_trees = 600 + redwood_count

    # return the result
    result = total_trees
    return result

print(solution())