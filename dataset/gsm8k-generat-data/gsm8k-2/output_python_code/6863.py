def solution():
    """Liezl prepared four sets of 2-dozen paper cups for her daughter's birthday party. If 5 cups were damaged and 30 were not used, how many paper cups were used?"""
    sets = 4
    cups_per_set = 2 * 12
    total_cups = sets * cups_per_set
    damaged_cups = 5
    unused_cups = 30
    used_cups = total_cups - damaged_cups - unused_cups
    result = used_cups
    return result

print(solution())