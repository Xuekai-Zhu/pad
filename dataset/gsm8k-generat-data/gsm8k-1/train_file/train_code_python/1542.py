def solution():
    """Ken can do 20 sit-ups without stopping. Nathan can do twice as many, and Bob can do half the number of Ken and Nathan's combined sit-ups. How many more sit-ups can Bob do compared to Ken?"""
    ken_situps = 20
    nathan_situps = ken_situps * 2
    combined_situps = ken_situps + nathan_situps
    bob_situps = combined_situps / 2
    difference = bob_situps - ken_situps
    result = difference
    return result

print(solution())