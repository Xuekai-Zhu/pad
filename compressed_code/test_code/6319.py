def solution():
    
    total_capacity = 16
    busy_capacity_percent = 50
    available_capacity_percent = 100 - busy_capacity_percent
    available_capacity = (available_capacity_percent / 100) * total_capacity
    result = available_capacity
    return result

print(solution())