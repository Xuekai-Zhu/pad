def solution():
    
    scallops_per_pound = 8
    cost_per_pound = 24.00
    scallops_per_person = 2
    num_people = 8
    total_scallops_needed = scallops_per_person * num_people
    total_pounds_needed = total_scallops_needed / scallops_per_pound
    total_cost = total_pounds_needed * cost_per_pound
    result = total_cost
    
    return result

print(solution())