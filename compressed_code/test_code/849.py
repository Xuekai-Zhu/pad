def solution():
    
    scallops_per_pound = 8
    price_per_pound = 24
    people = 8
    scallops_per_person = 2
    pounds_needed = (people * scallops_per_person) / scallops_per_pound
    total_cost = pounds_needed * price_per_pound
    result = total_cost
    return result

print(solution())