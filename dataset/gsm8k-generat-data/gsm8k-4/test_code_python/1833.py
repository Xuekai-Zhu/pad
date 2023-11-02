def solution():
    """Linda is repainting her bedroom. The wall area is 600 sq. ft. If a gallon of paint can cover 400 sq. ft., how many gallon cans of paint will Linda have to buy if she wants to do two coats?"""
    # Define the wall area and the coverage area of a gallon of paint
    wall_area = 600
    coverage_area = 400

    # Calculate the total paint needed for two coats
    total_paint = wall_area * 2 / coverage_area

    # Round up to the nearest gallon can of paint
    cans_needed = int(total_paint) + 1

    # Return the result
    result = cans_needed
    return result

print(solution())