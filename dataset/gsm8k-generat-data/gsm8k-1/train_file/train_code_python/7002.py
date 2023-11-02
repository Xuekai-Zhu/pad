def solution():
    """Julia bought 3 packs of red balls, 10 packs of yellow balls, and 8 packs of green balls. There were 19 balls in each package. How many balls did Julie buy in all?"""
    red_packs = 3
    yellow_packs = 10
    green_packs = 8
    balls_per_pack = 19
    total_balls = (red_packs + yellow_packs + green_packs) * balls_per_pack
    result = total_balls
    return result

print(solution())