def solution():
    """Mr. Maximilian is a dairy animal farmer and has 140 cows on his farm. Forty percent of the cows on his farm have a red spot, 25 percent of the cows without a red spot have a blue spot and the remaining cows do not have any spot. How many cows on the farm have no spot?"""
    # Define the total number of cows and the percentage with a red spot
    total_cows = 140
    red_spot_percentage = 0.4

    # Calculate the number of cows with a red spot
    red_spot_cows = total_cows * red_spot_percentage

    # Calculate the remaining number of cows and the percentage without a red spot
    remaining_cows = total_cows - red_spot_cows
    no_redspot_percentage = 1 - red_spot_percentage

    # Calculate the number of cows with a blue spot and without any spot
    blue_spot_cows = remaining_cows * 0.25
    no_spot_cows = remaining_cows - blue_spot_cows

    # Round the result and return it
    result = round(no_spot_cows)
    return result

print(solution())