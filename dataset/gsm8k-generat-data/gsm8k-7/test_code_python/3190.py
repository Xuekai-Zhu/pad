def solution():
    cost_per_trim = 5.0
    cost_per_fancy_trim = 15.0
    num_boxwoods = 30
    num_spheres = 4

    # Calculate the cost of trimming up all the boxwoods
    boxwoods_cost = num_boxwoods * cost_per_trim

    #Calculate the cost of shaping the 4 specific boxwoods into spheres
    sphere_cost = num_spheres * cost_per_fancy_trim

    # Calculate the total cost of all the work
    total_cost = boxwoods_cost + sphere_cost
    result = total_cost
    return result

print(solution())