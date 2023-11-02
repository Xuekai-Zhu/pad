def solution():
    
    total_towels = 3 + 6 + 3
    towels_per_load = 4
    loads_of_laundry = total_towels // towels_per_load + (total_towels % towels_per_load > 0)
    result = loads_of_laundry
    return result

print(solution())