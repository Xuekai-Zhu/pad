def solution():
    # Calculate the number of teaspoons Braelynn has
    teaspoons = 24 * 2  # twice as many teaspoons as knives

    # Calculate the number of additional knives Braelynn bought
    additional_knives = 24 * (1/3)  # 1/3 as many additional knives as initial knives

    # Calculate the number of additional teaspoons Braelynn bought
    additional_teaspoons = teaspoons * (2/3)  # 2/3 as many additional teaspoons as initial teaspoons

    # Calculate the total number of cutlery pieces she has in her kitchen
    total_cutlery = 24 + teaspoons + additional_knives + additional_teaspoons
    result = total_cutlery
    return result

print(solution())