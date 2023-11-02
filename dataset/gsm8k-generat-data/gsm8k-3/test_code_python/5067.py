def solution():
    """John is laying the foundation for 3 homes. Each home needs a slab of concrete that is 100 feet by 100 feet by .5 feet. Concrete has a density of 150 pounds per cubic foot. A pound of concrete cost $.02 per pound. How much does the foundation cost?"""
    # Define the dimensions of the slab
    LENGTH = 100
    WIDTH = 100
    HEIGHT = 0.5

    # Define the density and cost of concrete
    DENSITY = 150
    COST_PER_POUND = 0.02

    # Calculate the volume of one slab
    volume = LENGTH * WIDTH * HEIGHT

    # Calculate the weight of one slab
    weight = volume * DENSITY

    # Calculate the cost of one slab
    cost = weight * COST_PER_POUND

    # Calculate the total cost for all three slabs
    total_cost = cost * 3

    # Display the total cost
    result = total_cost
    return result

print(solution())