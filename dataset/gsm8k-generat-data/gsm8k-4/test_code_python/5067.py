def solution():
    """John is laying the foundation for 3 homes. Each home needs a slab of concrete that is 100 feet by 100 feet by .5 feet. Concrete has a density of 150 pounds per cubic foot. A pound of concrete cost $.02 per pound. How much does the foundation cost?"""
    # Define the dimensions of the slab of concrete
    length = 100  # in feet
    width = 100  # in feet
    height = 0.5  # in feet

    # Calculate the volume of the slab of concrete
    volume = length * width * height

    # Calculate the weight of the slab of concrete
    weight = volume * 150  # in pounds

    # Calculate the cost of the slab of concrete
    cost = weight * 0.02  # in dollars

    # Calculate the total cost of the foundations for 3 homes
    total_cost = cost * 3

    result = total_cost
    return result

print(solution())