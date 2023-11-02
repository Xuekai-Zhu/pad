def solution():
    # Calculate the total weight of the three adults
    adult_weight = 140 * 3

    # Calculate the total weight of the two children
    child_weight = 64 * 2

    # Calculate the total weight of everyone in the elevator so far
    total_weight = adult_weight + child_weight

    # Calculate the maximum weight allowed on the elevator
    max_weight = 600

    # Calculate the maximum weight of the next person who can get on the elevator
    max_next_weight = max_weight - total_weight
    result = max_next_weight
    return result

print(solution())