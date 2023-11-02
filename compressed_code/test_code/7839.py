def solution():
    
    num_bedroom_doors = 3
    num_outside_doors = 2
    cost_per_outside_door = 20
    cost_per_bedroom_door = cost_per_outside_door / 2
    total_cost = (num_outside_doors * cost_per_outside_door) + (num_bedroom_doors * cost_per_bedroom_door)
    result = total_cost

    return result

print(solution())