def solution():
    """John carves a giant marble rectangular prism 8 meters tall with a 2-meter square base.  It has a density of 2700 kg per cubic meter.  How much does it weigh?"""
    # Define the dimensions of the marble prism
    height = 8
    base = 2

    # Calculate the volume of the marble prism
    volume = height * (base ** 2)

    # Define the density of the marble
    density = 2700

    # Calculate the weight of the marble prism
    weight = volume * density

    # Display the weight of the marble prism
    result = weight
    return result

print(solution())