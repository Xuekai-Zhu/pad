def solution():
    # Calculate the number of children on the bus
    num_children = 0.25 * 60  

    # Calculate the number of adults on the bus
    num_adults = 60 - num_children
    result = num_adults
    return result

print(solution())