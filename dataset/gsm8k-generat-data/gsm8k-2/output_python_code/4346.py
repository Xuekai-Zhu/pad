def solution():
    """Braelynn has 24 knives in her kitchen and twice as many teaspoons as knives. 
    If she bought 1/3 as many additional knives and 2/3 as many additional teaspoons, 
    what would be the total number of cutlery pieces she has in her kitchen?"""
    knives = 24
    teaspoons = 2 * knives
    additional_knives = knives / 3
    additional_teaspoons = (2/3) * teaspoons
    total_cutlery = knives + teaspoons + additional_knives + additional_teaspoons
    result = total_cutlery
    return result

print(solution())