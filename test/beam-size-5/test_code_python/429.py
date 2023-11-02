def solution():
    
    total_gallons = 15
    containers = 5
    gallons_per_container = total_gallons / containers
    pints_per_container = gallons_per_container / 4
    pints_needed = pints_per_container * 8
    result = pints_needed
    return result

print(solution())