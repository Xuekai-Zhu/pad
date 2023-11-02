def solution():
     cubes_per_kabob = 4
     kabobs_needed = 40
     total_cubes_needed = cubes_per_kabob * kabobs_needed
     beef_slab_cost = 25
     beef_slab_cubes = 80
     cost_per_cube = beef_slab_cost / beef_slab_cubes
     total_cost = cost_per_cube * total_cubes_needed
     result = total_cost
     
     return result

print(solution())