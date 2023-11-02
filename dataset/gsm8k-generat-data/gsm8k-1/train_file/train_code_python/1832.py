def solution():
    """Linda is repainting her bedroom. The wall area is 600 sq. ft. If a gallon of paint can cover 400 sq. ft., how many gallon cans of paint will Linda have to buy if she wants to do two coats?"""
    wall_area = 600
    coverage_per_gallon = 400
    total_coverage_needed = wall_area * 2
    gallons_needed = total_coverage_needed / coverage_per_gallon
    result = gallons_needed
    return result

print(solution())