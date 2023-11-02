def solution():
    
    cubes_per_stick = 4
    cubes_per_slab = 80
    cost_per_slab = 25
    total_cubes_needed = cubes_per_stick * 40
    slabs_needed = total_cubes_needed / cubes_per_slab
    total_cost = slabs_needed * cost_per_slab
    result = total_cost
    return result

print(solution())