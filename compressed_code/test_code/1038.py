def solution():
    
    cubes_per_stick = 4
    total_sticks = 40
    cubes_per_slab = 80
    cost_per_slab = 25
    total_cubes_needed = cubes_per_stick * total_sticks
    total_slabs_needed = total_cubes_needed / cubes_per_slab
    total_cost = total_slabs_needed * cost_per_slab
    result = total_cost
    return result

print(solution())