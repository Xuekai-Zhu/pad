def solution():
    original_steak = 30  # ounces
    burned_steak = original_steak / 2
    remaining_steak = original_steak - burned_steak
    eaten_steak = 0.8 * remaining_steak
    result = eaten_steak
    return result

print(solution())