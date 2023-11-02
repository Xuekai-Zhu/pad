def solution():
    """Mr. Maximilian is a dairy animal farmer and has 140 cows on his farm. Forty percent of the cows on his farm have a red spot, 25 percent of the cows without a red spot have a blue spot and the remaining cows do not have any spot. How many cows on the farm have no spot?"""
    total_cows = 140
    red_spots = total_cows * 0.4
    cows_without_red_spots = total_cows - red_spots
    blue_spots = cows_without_red_spots * 0.25
    cows_without_spots = total_cows - red_spots - blue_spots
    result = cows_without_spots
    return result

print(solution())