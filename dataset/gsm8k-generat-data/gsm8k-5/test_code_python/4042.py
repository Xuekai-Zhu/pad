def solution():
    land_cost_per_square_meter = 20  # Land costs $20 per square meter
    total_land_cost = 8000 + 4000  # Carlson spent $8000 on the first piece of land and $4000 on the second piece of land
    total_land_area = total_land_cost / land_cost_per_square_meter  # Calculate the total area of his land

    # Add the initial land area to the total land area
    total_land_area += 300

    result = total_land_area
    return result

print(solution())