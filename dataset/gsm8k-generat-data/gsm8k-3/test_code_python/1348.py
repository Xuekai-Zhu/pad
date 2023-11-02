def solution():
    """A single kabob stick has 4 cubes of beef. A slab of beef that costs $25 can be cut into 80 cubes. How much must Simon spend to make 40 kabob sticks?"""
    # Define the number of cubes of beef per kabob stick
    CUBES_PER_STICK = 4

    # Define the cost of a slab of beef and the number of cubes it can be cut into
    SLAB_COST = 25
    SLAB_CUBES = 80

    # Calculate the number of cubes of beef needed for 40 kabob sticks
    total_cubes = 40 * CUBES_PER_STICK

    # Calculate the number of slabs of beef needed
    total_slabs = total_cubes / SLAB_CUBES

    # Calculate the total cost of the slabs of beef
    total_cost = total_slabs * SLAB_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())