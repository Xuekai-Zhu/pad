def solution():
    """Three adults whose average weight is 140 pounds went first in the elevator. Two children whose average weight is 64 pounds also went inside. If an elevator sign reads “Maximum weight 600 pounds.", what is the maximum weight of the next person to get in the elevator so that it will not be overloaded?"""
    # Define the weights of the adults and children
    adult_weights = [140, 140, 140]
    child_weights = [64, 64]

    # Calculate the total weight of the adults and children already in the elevator
    total_weight = sum(adult_weights) + sum(child_weights)

    # Calculate the maximum weight limit for the next person to get in the elevator
    max_weight = 600 - total_weight

    # Display the maximum weight limit
    result = max_weight
    return result

print(solution())