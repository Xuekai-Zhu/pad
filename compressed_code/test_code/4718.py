def solution():
    
    original_steak = 30
    burned_steak = original_steak / 2
    edible_steak = original_steak - burned_steak
    eaten_steak = 0.8 * edible_steak
    result = eaten_steak
    return result

print(solution())