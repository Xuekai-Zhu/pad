def solution():
    """Matt can paint a house in 12 hours. Patty can paint the same house in one third the time. Rachel can paint the same house in 5 more than double the amount of hours as Patty. How long will it take Rachel to paint the house?"""
    # Define the time it takes for Matt to paint the house
    matt_time = 12

    # Define the time it takes for Patty to paint the house
    patty_time = matt_time / 3

    # Define the time it takes for Rachel to paint the house
    rachel_time = (2 * patty_time) + 5

    result = rachel_time
    return result

print(solution())