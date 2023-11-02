def solution():
    knives = 24  # Braelynn has 24 knives
    teaspoons = knives * 2  # Braelynn has twice as many teaspoons as knives

    # Calculate the additional knives
    additional_knives = knives / 3

    # Calculate the additional teaspoons
    additional_teaspoons = teaspoons * 2 / 3

    # Calculate the total number of cutlery pieces
    total_cutlery = knives + additional_knives + teaspoons + additional_teaspoons
    result = total_cutlery
    return result

print(solution())