def solution():
    total_area = 1110
    bedroom_area = 4 * (11 * 11)
    bathroom_area = 2 * (6 * 8)
    remaining_area = total_area - bedroom_area - bathroom_area

    # Divide the remaining area by 2 since the kitchen and living area have the same size
    kitchen_area = remaining_area / 2
    result = kitchen_area
    return result

print(solution())