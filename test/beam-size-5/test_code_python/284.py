def solution():
    
    flagstone_weight = 75
    total_weight = 2000
    flagstones_per_trip = 80
    trucks_needed = (total_weight - (flagstone_weight * flagstones_per_trip)) / flagstone_weight
    result = trucks_needed
    return result

print(solution())