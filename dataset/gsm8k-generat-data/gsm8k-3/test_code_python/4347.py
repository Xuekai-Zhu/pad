def solution():
    """Braelynn has 24 knives in her kitchen and twice as many teaspoons as knives. If she bought 1/3 as many additional knives and 2/3 as many additional teaspoons, what would be the total number of cutlery pieces she has in her kitchen?"""
    # Define the number of knives and teaspoons that Braelynn has
    knives = 24
    teaspoons = knives * 2

    # Calculate the number of additional knives and teaspoons Braelynn bought
    additional_knives = knives * (1/3)
    additional_teaspoons = teaspoons * (2/3)

    # Calculate the total number of cutlery pieces Braelynn has
    total_cutlery = knives + teaspoons + additional_knives + additional_teaspoons

    # Display the total number of cutlery pieces
    result = total_cutlery
    return result

print(solution())