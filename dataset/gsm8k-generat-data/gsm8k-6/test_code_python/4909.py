def solution():
    # Calculate the number of cows with a red spot
    red_cows = 0.4 * 140

    # Calculate the number of cows without a red spot
    no_red_cows = 140 - red_cows

    # Calculate the number of cows with a blue spot
    blue_cows = 0.25 * no_red_cows

    # Calculate the number of cows with no spot
    no_spot_cows = no_red_cows - blue_cows

    result = no_spot_cows
    return result

print(solution())