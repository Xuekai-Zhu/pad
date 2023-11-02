def solution():
    
    s_mores_per_person = 3
    total_people = 8
    s_mores_total = s_mores_per_person * total_people
    s_mores_per_batch = 4
    batches_needed = s_mores_total / s_mores_per_batch
    cost_per_batch = 3
    total_cost = batches_needed * cost_per_batch
    result = total_cost
    return result

print(solution())