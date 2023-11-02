def solution():
    num_initial_cabinets = 3
    num_counters = 3
    num_added_cabinets_per_counter = 2
    num_added_cabinets = 5

    # Calculate the total number of cabinets over the 3 counters
    total_added_cabinets = num_counters * num_added_cabinets_per_counter

    # Calculate the total number of cabinets Jeff has now
    total_cabinets = num_initial_cabinets + total_added_cabinets + num_added_cabinets
    result = total_cabinets
    return result

print(solution())