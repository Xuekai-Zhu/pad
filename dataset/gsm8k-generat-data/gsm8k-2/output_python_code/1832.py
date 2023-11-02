def solution():
    """Linda is repainting her bedroom. The wall area is 600 sq. ft. If a gallon of paint can cover 400 sq. ft., how many gallon cans of paint will Linda have to buy if she wants to do two coats?"""
    wall_area = 600
    coverage_per_gallon = 400
    total_coverage = wall_area * 2
    cans_of_paint = total_coverage / coverage_per_gallon
    result = cans_of_paint
    return result

print(solution())