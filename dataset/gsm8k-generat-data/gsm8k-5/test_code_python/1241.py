def solution():
    height = 8  # The height of the rectangular prism is 8 meters
    base_length = 2  # The length and width of the base are both 2 meters
    base_width = 2
    density = 2700  # The density of the marble is 2700 kg per cubic meter

    # Calculate the volume of the rectangular prism
    volume = height * base_length * base_width

    # Calculate the weight of the rectangular prism
    weight = volume * density
    result = weight
    return result

print(solution())