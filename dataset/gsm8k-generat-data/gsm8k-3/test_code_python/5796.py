def solution():
    """Bob is building a vegetable garden. It is 220 feet long by 120 feet wide. Half of the garden is going to be tilled land. A third of the rest of it will have trellises for vining plants, and the rest will be devoted to raised beds. How big will the raised bed section of the garden be?"""
    # Define the dimensions of the garden
    length = 220
    width = 120

    # Calculate the area of the garden
    total_area = length * width

    # Calculate the area of the tilled land
    tilled_land_area = total_area / 2

    # Calculate the area of the land not used for tilled land
    remaining_area = total_area - tilled_land_area

    # Calculate the area of the trellises
    trellis_area = remaining_area / 3

    # Calculate the area of the raised beds
    raised_bed_area = remaining_area - trellis_area

    # Display the area of the raised beds
    result = raised_bed_area
    return result

print(solution())