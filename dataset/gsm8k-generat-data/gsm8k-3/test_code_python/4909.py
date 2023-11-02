def solution():
    """Mr. Maximilian is a dairy animal farmer and has 140 cows on his farm. Forty percent of the cows on his farm have a red spot, 25 percent of the cows without a red spot have a blue spot and the remaining cows do not have any spot. How many cows on the farm have no spot?"""
    # Define the total number of cows on the farm
    total_cows = 140

    # Calculate the number of cows with a red spot
    red_spot_cows = 0.4 * total_cows

    # Calculate the number of cows without a red spot
    non_red_spot_cows = total_cows - red_spot_cows

    # Calculate the number of cows with a blue spot
    blue_spot_cows = 0.25 * non_red_spot_cows

    # Calculate the number of cows with no spot
    no_spot_cows = total_cows - red_spot_cows - blue_spot_cows

    # Display the number of cows with no spot
    result = no_spot_cows
    return result

print(solution())