def solution():
    
    points_needed = 2000
    points_from_bunnies = 8 * 100
    points_from_snickers = points_needed - points_from_bunnies
    snickers_per_point = 1/25
    snickers_needed = points_from_snickers * snickers_per_point
    result = snickers_needed
    return result

print(solution())