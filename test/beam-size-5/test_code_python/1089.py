def solution():
    
    north_wall_area = 10 * 8
    east_wall_area = 5 * 8
    total_area = north_wall_area + east_wall_area
    gallons_of_paint = total_area / 20
    cost_per_gallon = 12
    total_cost = gallons_of_paint * cost_per_gallon
    result = total_cost
    return result

print(solution())