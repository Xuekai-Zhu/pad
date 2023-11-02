def solution():
    """Kate bought 7 packs of red bouncy balls and 6 packs of yellow bouncy balls. Each pack contained 18 bouncy balls. How many more red bouncy balls than yellow bouncy balls did Kate buy?"""
    # Define the number of packs of each color of bouncy balls
    RED_PACKS = 7
    YELLOW_PACKS = 6

    # Define the number of bouncy balls per pack
    BALLS_PER_PACK = 18

    # Calculate the total number of red bouncy balls
    red_balls = RED_PACKS * BALLS_PER_PACK

    # Calculate the total number of yellow bouncy balls
    yellow_balls = YELLOW_PACKS * BALLS_PER_PACK

    # Calculate the difference between the number of red and yellow bouncy balls
    diff = red_balls - yellow_balls

    # Display the difference
    result = diff
    return result

print(solution())