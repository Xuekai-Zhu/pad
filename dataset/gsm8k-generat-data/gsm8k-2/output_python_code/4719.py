def solution():
    """Cara has 60 marbles in a bag. 20 of them are yellow, half as many are green, and the remaining marbles are equally divided between red and blue. If Cara picks a marble at random, what are the odds it's blue (expressed as a percentage)?"""
    total_marbles = 60
    yellow_marbles = 20
    green_marbles = yellow_marbles / 2
    red_blue_marbles = total_marbles - yellow_marbles - green_marbles
    blue_marbles = red_blue_marbles / 2
    blue_odds = (blue_marbles / total_marbles) * 100
    result = blue_odds
    return result

print(solution())