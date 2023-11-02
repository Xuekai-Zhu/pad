def solution():
    
    initial_cabinets = 3
    num_counters = 3
    additional_cabinets = num_counters * 2 * initial_cabinets
    total_cabinets = initial_cabinets + additional_cabinets + 5
    result = total_cabinets
    return result

print(solution())