def solution():
    
    fabric_available = 56
    fabric_per_dress = 4
    dresses_possible = fabric_available // fabric_per_dress
    hours_per_dress = 3
    total_hours = dresses_possible * hours_per_dress
    result = total_hours
    return result

print(solution())