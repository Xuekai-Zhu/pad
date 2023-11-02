def solution():
    # Calculate the area of the bathroom in square inches
    width = 10  # number of tiles along width
    length = 20  # number of tiles along length
    area_inches = width * length * 6 * 6  # area in square inches

    # Convert square inches to square footage
    area_footage = area_inches / (12 * 12)
    result = area_footage
    return result

print(solution())