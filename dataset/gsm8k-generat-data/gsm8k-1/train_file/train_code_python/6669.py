def solution():
    """Three blue chips are in a jar which is 10% of the entire chips. If 50% of the chips are white and the rest are green, how many green chips are there?"""
    total_chips = 10 / 0.1  # 100 chips in total
    blue_chips = 3
    white_chips = total_chips * 0.5
    green_chips = total_chips - blue_chips - white_chips
    result = green_chips
    return result

print(solution())