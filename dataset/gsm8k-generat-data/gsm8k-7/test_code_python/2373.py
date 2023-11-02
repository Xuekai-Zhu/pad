def solution():
    total_passengers = 60
    children_percentage = 0.25

    # Calculate the number of children on the bus
    num_children = total_passengers * children_percentage

    # Calculate the number of adults on the bus
    num_adults = total_passengers - num_children

    result = num_adults
    return result

print(solution())