def solution():
    # Calculate the volume of the rectangular prism
    volume = 8 * 2 * 2  # height times base length times base width
    # Calculate the weight of the marble block
    weight = volume * 2700  # density (kg per cubic meter) times volume (cubic meters)
    result = weight
    return result

print(solution())