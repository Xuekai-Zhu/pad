def solution():
    total_cows = 140  # Mr. Maximilian has 140 cows on his farm

    # Calculate the number of cows with a red spot
    cows_with_red_spot = 0.4 * total_cows

    # Calculate the number of cows without a red spot
    cows_without_red_spot = total_cows - cows_with_red_spot

    # Calculate the number of cows with a blue spot
    cows_with_blue_spot = 0.25 * cows_without_red_spot

    # Calculate the number of cows without any spot
    cows_with_no_spot = total_cows - cows_with_red_spot - cows_with_blue_spot

    result = cows_with_no_spot
    return result

print(solution())