def solution():
    property_width = 1000
    property_length = 2250

    # Calculate the width of the garden
    garden_width = property_width / 8

    # Calculate the length of the garden
    garden_length = property_length / 10

    # Calculate the area of the garden
    garden_area = garden_width * garden_length
    result = garden_area
    return result

print(solution())