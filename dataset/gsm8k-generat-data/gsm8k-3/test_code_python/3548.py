def solution():
    """Amanda is figuring out how many bags of grass seed she needs to buy to cover a new lot the city is turning into a park. The lot measures 120 feet by 60 feet. One section that measures 40 feet by 40 feet will be covered with concrete, and the rest needs to be covered in grass seeds. Each bag of grass seeds covers 56 square feet. How many bags of grass seeds does Amanda need?"""
    # Define the area of the lot and the area of the section to be covered in concrete
    total_area = 120 * 60
    concrete_area = 40 * 40

    # Calculate the area to be covered in grass seeds
    grass_area = total_area - concrete_area

    # Calculate the number of bags of grass seeds needed
    bags_needed = grass_area / 56

    # Round up to the nearest whole bag
    bags_needed = math.ceil(bags_needed)

    # Display the number of bags of grass seeds needed
    result = bags_needed
    return result

print(solution())