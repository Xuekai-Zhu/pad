def solution():
    """A single kabob stick has 4 cubes of beef. A slab of beef that costs $25 can be cut into 80 cubes. How much must Simon spend to make 40 kabob sticks?"""
    # Define the number of cubes needed for one kabob stick
    cubes_per_kabob = 4

    # Define the cost of a slab of beef and the number of cubes it can be cut into
    slab_cost = 25
    cubes_per_slab = 80

    # Calculate the total number of cubes needed for 40 kabob sticks
    total_cubes = 40 * cubes_per_kabob

    # Calculate the number of slabs needed to get the required number of cubes
    total_slabs = total_cubes / cubes_per_slab

    # Calculate the total cost of the required amount of beef
    total_cost = total_slabs * slab_cost

    result = total_cost
    return result

print(solution())