def solution():
    
    fabric_per_dress = 4
    hours_per_dress = 3
    fabric_available = 56
    total_dresses = fabric_available // fabric_per_dress
    total_hours = total_dresses * hours_per_dress
    result = total_hours
    return result

print(solution())