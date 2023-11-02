def solution():
    num_cubes_per_slab = 80
    cost_per_slab = 25
    cubes_per_kabob = 4
    num_kabobs = 40

    # Calculate the total number of cubes of beef needed
    total_cubes = cubes_per_kabob * num_kabobs

    # Calculate the total number of slabs of beef needed
    num_slabs = total_cubes / num_cubes_per_slab
    if total_cubes % num_cubes_per_slab != 0:
        num_slabs += 1

    # Calculate the total cost of all slabs of beef needed
    total_cost = num_slabs * cost_per_slab
    result = total_cost
    return result

print(solution())