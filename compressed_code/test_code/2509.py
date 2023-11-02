def solution():
    
    total_area = 1110
    bedroom_area = 4 * (11 * 11)
    bathroom_area = 2 * (6 * 8)
    living_area = total_area - bedroom_area - bathroom_area
    kitchen_area = living_area / 2
    result = kitchen_area
    return result

print(solution())