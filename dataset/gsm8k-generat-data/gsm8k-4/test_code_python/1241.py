def solution():
    """John carves a giant marble rectangular prism 8 meters tall with a 2-meter square base. It has a density of 2700 kg per cubic meter. How much does it weigh?"""
    # Define the dimensions of the rectangular prism
    height = 8
    base_length = 2
    base_width = 2

    # Calculate the volume of the rectangular prism
    volume = height * base_length * base_width

    # Calculate the weight of the rectangular prism given its density
    density = 2700
    weight = volume * density

    result = weight
    return result

print(solution())