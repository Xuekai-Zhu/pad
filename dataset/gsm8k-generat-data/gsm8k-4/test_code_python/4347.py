def solution():
    """Braelynn has 24 knives in her kitchen and twice as many teaspoons as knives. If she bought 1/3 as many additional knives and 2/3 as many additional teaspoons, what would be the total number of cutlery pieces she has in her kitchen?"""
    # Calculate the number of teaspoons
    teaspoons = 24 * 2

    # Calculate the number of additional knives
    additional_knives = 24 * (1/3)

    # Calculate the number of additional teaspoons
    additional_teaspoons = teaspoons * (2/3)

    # Calculate the total number of cutlery pieces
    total_cutlery = 24 + teaspoons + additional_knives + additional_teaspoons

    # return the result
    result = total_cutlery
    return result

print(solution())