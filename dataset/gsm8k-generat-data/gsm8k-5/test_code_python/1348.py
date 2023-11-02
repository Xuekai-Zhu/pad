def solution():
    cubes_per_kabob = 4  # Each kabob stick requires 4 cubes of beef
    cubes_per_slab = 80  # A slab of beef can be cut into 80 cubes
    cost_per_slab = 25  # The slab of beef costs $25

    # Calculate the total number of cubes of beef needed for 40 kabob sticks
    total_cubes = cubes_per_kabob * 40

    # Calculate the total number of slabs of beef needed
    total_slabs = total_cubes / cubes_per_slab

    # Calculate the total cost of the beef needed
    total_cost = total_slabs * cost_per_slab
    result = total_cost
    return result

print(solution())