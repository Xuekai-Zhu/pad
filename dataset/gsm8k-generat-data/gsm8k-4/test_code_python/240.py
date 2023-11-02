def solution():
    """Kate bought 7 packs of red bouncy balls and 6 packs of yellow bouncy balls. Each pack contained 18 bouncy balls. How many more red bouncy balls than yellow bouncy balls did Kate buy?"""
    # Define the number of packs and the number of balls per pack
    RED_PACKS = 7
    YELLOW_PACKS = 6
    BALLS_PER_PACK = 18

    # Calculate the total number of red and yellow bouncy balls
    red_balls = RED_PACKS * BALLS_PER_PACK
    yellow_balls = YELLOW_PACKS * BALLS_PER_PACK

    # Calculate the difference in the number of red and yellow bouncy balls
    difference = red_balls - yellow_balls

    result = difference
    return result

print(solution())