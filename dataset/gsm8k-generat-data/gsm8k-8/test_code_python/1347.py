def solution():
    # Calculate the number of cabinets over one counter
    cabinets_per_counter = 3

    # Calculate the number of cabinets over three counters
    cabinets_over_three_counters = 2 * cabinets_per_counter * 3

    # Calculate the total number of cabinets
    total_cabinets = cabinets_per_counter + cabinets_over_three_counters + 5
    result = total_cabinets
    return result

print(solution())