def solution():
    wall_area = 600  # The wall area is 600 sq. ft.
    coverage_per_gallon = 400  # A gallon of paint covers 400 sq. ft.
    coats = 2  # Linda wants to do two coats of paint

    # Calculate the total paint coverage required for two coats
    total_coverage = wall_area * coats

    # Calculate the number of gallon cans required
    cans_required = total_coverage / coverage_per_gallon
    result = cans_required
    return result

print(solution())