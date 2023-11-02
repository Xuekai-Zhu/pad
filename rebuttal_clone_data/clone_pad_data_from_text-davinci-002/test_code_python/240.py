def solution():
    """Kate bought 7 packs of red bouncy balls and 6 packs of yellow bouncy balls. Each pack contained 18 bouncy balls. How many more red bouncy balls than yellow bouncy balls did Kate buy?"""
    packs_red = 7
    packs_yellow = 6
    bouncy_balls_per_pack = 18
    total_red_bouncy_balls = packs_red * bouncy_balls_per_pack
    total_yellow_bouncy_balls = packs_yellow * bouncy_balls_per_pack
    difference = total_red_bouncy_balls - total_yellow_bouncy_balls
    result = difference
    return result

print(solution())