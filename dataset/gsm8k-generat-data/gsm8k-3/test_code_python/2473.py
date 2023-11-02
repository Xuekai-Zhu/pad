def solution():
    """Matt can paint a house in 12 hours.  Patty can paint the same house in one third the time.  Rachel can paint the same house in 5 more than double the amount of hours as Patty. How long will it take Rachel to paint the house?"""
    # Define the time it takes Matt to paint the house
    MATT_TIME = 12

    # Define the time it takes Patty to paint the house
    PATTY_TIME = MATT_TIME / 3

    # Define the time it takes Rachel to paint the house
    RACHEL_TIME = (2 * PATTY_TIME) + 5

    # Display the time it takes Rachel to paint the house
    result = RACHEL_TIME
    return result

print(solution())