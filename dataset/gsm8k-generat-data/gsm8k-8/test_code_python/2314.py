def solution():
    # Define Tyler's weight in terms of Sam's weight
    tyler_weight = sam_weight + 25

    # Define Peter's weight in terms of Tyler's weight
    peter_weight = tyler_weight / 2

    # Use the given weight of Peter to calculate Tyler's weight
    tyler_weight = peter_weight * 2

    # Use Tyler's weight to calculate Sam's weight
    sam_weight = tyler_weight - 25

    result = sam_weight
    return result

print(solution())