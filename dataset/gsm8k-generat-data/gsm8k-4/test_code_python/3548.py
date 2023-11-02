def solution():
    """Amanda is figuring out how many bags of grass seed she needs to buy to cover a new lot the city is turning into a park. The lot measures 120 feet by 60 feet. One section that measures 40 feet by 40 feet will be covered with concrete, and the rest needs to be covered in grass seeds. Each bag of grass seeds covers 56 square feet. How many bags of grass seeds does Amanda need?"""
    # Define the dimensions of the lot and the concrete section
    lot_length = 120
    lot_width = 60
    concrete_length = 40
    concrete_width = 40

    # Calculate the area of the lot and the area of the concrete section
    lot_area = lot_length * lot_width
    concrete_area = concrete_length * concrete_width

    # Calculate the area of the grass section
    grass_area = lot_area - concrete_area

    # Calculate the number of bags of grass seeds needed, rounded up to the nearest whole number
    bags_needed = math.ceil(grass_area / 56)

    # Return the result
    result = bags_needed
    return result

print(solution())