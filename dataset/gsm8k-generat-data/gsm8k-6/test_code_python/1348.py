def solution():
    # Calculate the number of cubes of beef needed to make 40 kabob sticks
    cubes_per_kabob = 4
    total_cubes = cubes_per_kabob * 40

    # Calculate the cost of the required number of cubes of beef
    cubes_cost = 25/80  # cost per cube
    total_cost = cubes_cost * total_cubes
    result = total_cost
    return result

print(solution())