def solution():
    """A single kabob stick has 4 cubes of beef. A slab of beef that costs $25 can be cut into 80 cubes. How much must Simon spend to make 40 kabob sticks?"""
    cubes_per_stick = 4
    cubes_per_slab = 80
    cost_per_slab = 25
    total_cubes_needed = cubes_per_stick * 40
    slabs_needed = total_cubes_needed / cubes_per_slab
    total_cost = slabs_needed * cost_per_slab
    result = total_cost
    return result

print(solution())