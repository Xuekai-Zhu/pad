def solution():
    
    total_days = 180
    capsules_per_serv = 2
    capsules_per_bottle = 60
    total_servings = total_days * capsules_per_serv
    total_bottles = total_servings // capsules_per_bottle
    if total_servings % capsules_per_bottle != 0:
        total_bottles += 1
    result = total_bottles
    return result

print(solution())