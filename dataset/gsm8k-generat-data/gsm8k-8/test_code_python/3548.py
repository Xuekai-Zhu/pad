def solution():
    # Calculate the area of the entire lot
    total_area = 120 * 60

    # Calculate the area of the section that will be covered in concrete
    concrete_area = 40 * 40

    # Calculate the area that needs to be covered in grass seeds
    grass_area = total_area - concrete_area

    # Calculate the number of bags of grass seeds needed
    bags_needed = grass_area / 56

    result = bags_needed
    return result

print(solution())