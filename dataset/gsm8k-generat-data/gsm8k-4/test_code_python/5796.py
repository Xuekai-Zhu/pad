def solution():
    """Bob is building a vegetable garden. It is 220 feet long by 120 feet wide. Half of the garden is going to be tilled land. A third of the rest of it will have trellises for vining plants, and the rest will be devoted to raised beds. How big will the raised bed section of the garden be?"""
    # Define the dimensions of the garden
    length = 220
    width = 120

    # Calculate the area of the garden
    garden_area = length * width

    # Calculate the area of the tilled land
    tilled_area = garden_area / 2

    # Calculate the area of the part of the garden with trellises
    trellis_area = (garden_area - tilled_area) / 3

    # Calculate the area of the raised bed section
    raised_bed_area = garden_area - tilled_area - trellis_area

    # Return the result
    result = raised_bed_area
    return result

print(solution())