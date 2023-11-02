def solution():
    num_adults = 3
    avg_adult_weight = 140
    num_children = 2
    avg_child_weight = 64
    max_weight = 600

    # Calculate the total weight of the adults
    total_adult_weight = num_adults * avg_adult_weight

    # Calculate the total weight of the children
    total_child_weight = num_children * avg_child_weight

    # Calculate the current weight in the elevator
    current_weight = total_adult_weight + total_child_weight

    # Calculate the maximum weight that the elevator can carry without being overloaded
    max_weight_remaining = max_weight - current_weight

    # Calculate the maximum weight of the next person that can get in the elevator
    max_next_weight = max_weight_remaining
    result = max_next_weight
    return result

print(solution())