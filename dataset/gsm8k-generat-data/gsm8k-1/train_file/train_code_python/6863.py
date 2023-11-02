def solution():
    """Liezl prepared four sets of 2-dozen paper cups for her daughter's birthday party. If 5 cups were damaged and 30 were not used, how many paper cups were used?"""
    paper_cups_per_set = 24
    sets_prepared = 4
    damaged_cups = 5
    unused_cups = 30
    total_cups = paper_cups_per_set * sets_prepared
    cups_used = total_cups - damaged_cups - unused_cups
    result = cups_used
    return result

print(solution())