def solution():
    """Three adults whose average weight is 140 pounds went first in the elevator. Two children whose average weight is 64 pounds also went inside. 
    If an elevator sign reads “Maximum weight 600 pounds.", what is the maximum weight of the next person to get in the elevator so that it will not be overloaded?"""
    # Define the weights of the people who are already in the elevator
    adults_weight = 140 * 3
    children_weight = 64 * 2
    total_weight = adults_weight + children_weight

    # Calculate the maximum weight that can be added to the elevator
    max_weight = 600 - total_weight

    # Return the result
    result = max_weight
    return result

print(solution())