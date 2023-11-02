def solution():
    """In a national park, the number of redwoods is 20% more than the number of pines. If there are 600 pines in the national park, calculate the total number of pines and redwoods that are there."""
    # Define the percentage increase of the redwoods compared to the pines
    REDWOOD_INCREASE = 0.2

    # Get the number of pines in the park
    num_pines = 600

    # Calculate the number of redwoods in the park
    num_redwoods = num_pines * (1 + REDWOOD_INCREASE)

    # Calculate the total number of trees in the park
    total_trees = num_pines + num_redwoods

    # Display the total number of trees in the park
    result = total_trees
    return result

print(solution())