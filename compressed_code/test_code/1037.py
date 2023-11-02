def solution():
    
    starting_cabinets = 3
    additional_cabinets_per_counter = 2 * starting_cabinets
    counters = 3
    total_additional_cabinets = additional_cabinets_per_counter * counters
    additional_cabinets = 5
    total_cabinets = starting_cabinets + total_additional_cabinets + additional_cabinets
    result = total_cabinets
    return result

print(solution())