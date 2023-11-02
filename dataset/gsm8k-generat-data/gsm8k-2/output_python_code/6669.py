def solution():
    """Three blue chips are in a jar which is 10% of the entire chips. If 50% of the chips are white and the rest are green, how many green chips are there?"""
    total_chips = 100  # assume there are 100 chips in total
    blue_chips = 3
    jar_percentage = 10
    white_percentage = 50
    green_percentage = 100 - jar_percentage - white_percentage
    green_chips = (green_percentage / 100) * (total_chips - blue_chips)
    result = green_chips
    return result

print(solution())