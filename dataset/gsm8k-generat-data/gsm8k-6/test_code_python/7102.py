def solution():
    # Calculate the width and length of the vegetable garden
    garden_width = 1000/8  # width of the garden is 1/8 of the property width
    garden_length = 2250/10  # length of the garden is 1/10 of the property length

    # Calculate the area of the garden
    garden_area = garden_width * garden_length

    result = garden_area
    return result

print(solution())