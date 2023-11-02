def solution():
    """Adam has 50 balls. 20 balls are red, 10 are blue, and the rest are either pink or orange. If there are 3 times as many pink as orange balls, how many orange balls are there?"""
    total_balls = 50
    red_balls = 20
    blue_balls = 10
    pink_orange_balls = total_balls - red_balls - blue_balls
    pink_balls = 3 * pink_orange_balls / 4
    orange_balls = pink_orange_balls / 4
    result = orange_balls
    return result

print(solution())