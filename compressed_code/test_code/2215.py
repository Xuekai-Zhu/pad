def solution():
    
    total_area = 1600
    gallons_needed = (total_area / 400) * 2
    cost_per_person = (gallons_needed * 45) / 2
    result = cost_per_person
    return result

print(solution())