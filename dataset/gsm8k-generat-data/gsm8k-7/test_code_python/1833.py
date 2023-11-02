def solution():
    wall_area = 600
    coverage_per_gallon = 400
    coats = 2

    # Calculate the total area to be covered
    total_area = wall_area * coats

    # Calculate the total number of gallons needed
    gallons_needed = total_area / coverage_per_gallon

    # Round up to the nearest whole gallon
    gallons_needed = math.ceil(gallons_needed)

    result = gallons_needed
    return result

print(solution())