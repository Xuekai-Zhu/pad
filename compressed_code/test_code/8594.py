def solution():
    
    total_area = 120 * 60
    concrete_area = 40 * 40
    grass_area = total_area - concrete_area
    bags_needed = grass_area / 56
    result = bags_needed
    return result

print(solution())