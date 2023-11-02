def solution():
    current_height = 180
    growth_factor = 0.5  # 50% taller
    original_height = current_height / (1 + growth_factor)  # original height can be calculated using proportion
    original_height_feet = original_height / 12  # convert to feet
    result = original_height_feet
    return result

print(solution())