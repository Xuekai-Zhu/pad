def solution():
    # Calculate the total number of cabinets that Jeff has
    initial_cabinets = 3  # number of cabinets over one counter
    new_cabinets = 2 * 3  # number of cabinets over three counters
    total_cabinets = initial_cabinets + new_cabinets + 5  # add the new cabinets
    result = total_cabinets
    return result

print(solution())