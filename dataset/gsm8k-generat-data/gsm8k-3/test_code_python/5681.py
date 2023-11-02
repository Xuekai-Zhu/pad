def solution():
    """Jill bought 5 packs of red bouncy balls and 4 packs of yellow bouncy balls. Each package contained 18 bouncy balls. How many more red bouncy balls than yellow bouncy balls did Jill buy?"""
    # Define the number of packs and bouncy balls in each pack
    RED_PACKS = 5
    YELLOW_PACKS = 4
    BALLS_PER_PACK = 18

    # Calculate the total number of red and yellow bouncy balls
    red_balls = RED_PACKS * BALLS_PER_PACK
    yellow_balls = YELLOW_PACKS * BALLS_PER_PACK

    # Calculate the difference between the number of red and yellow bouncy balls
    difference = red_balls - yellow_balls

    # Display the difference between the number of red and yellow bouncy balls
    result = difference
    return result

print(solution())