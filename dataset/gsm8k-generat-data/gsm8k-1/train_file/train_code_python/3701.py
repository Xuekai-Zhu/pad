def solution():
    """Janet is considering two options to retile her bathroom. The turquoise tiles cost $13/tile and the purple tiles cost $11/tile. If Janet needs to tile two walls that measure 5 feet by 8 feet and 7 feet by 8 feet, and each square foot of wall takes 4 tiles, how much will Janet save by buying the purple tiles instead of the turquoise ones?"""
    turquoise_cost = 13
    purple_cost = 11
    wall1_area = 5 * 8
    wall2_area = 7 * 8
    total_area = wall1_area + wall2_area
    tiles_needed = total_area * 4
    turquoise_total_cost = turquoise_cost * tiles_needed
    purple_total_cost = purple_cost * tiles_needed
    savings = turquoise_total_cost - purple_total_cost
    result = savings
    
    return result

print(solution())