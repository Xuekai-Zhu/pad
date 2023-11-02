def solution():
    # Calculate the total number of builders needed for 5 houses with 6 floors each
    total_builders = 3 * 6 * 5 * 6  # Three builders per floor, 6 floors per house, and 5 houses

    # Calculate the total number of days needed to complete the job with the new number of builders
    total_days = (30 * 3 * 6 * 5 * 6) / total_builders

    # Calculate the total cost of hiring the 6 builders for the job
    total_cost = total_builders * total_days * 100

    result = total_cost
    return result

print(solution())