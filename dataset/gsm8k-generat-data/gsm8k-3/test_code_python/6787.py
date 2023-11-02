def solution():
    """Koby and Cherie want to light fireworks. Koby has bought 2 boxes of fireworks while Cherie has just 1 box of fireworks. Koby’s boxes each contain 3 sparklers and 5 whistlers. Cherie’s box has 8 sparklers and 9 whistlers. In total, how many fireworks do Koby and Cherie have?"""
    # Define the number of boxes and contents of each box
    KOBYS_BOXES = 2
    KOBYS_SPARKLERS_PER_BOX = 3
    KOBYS_WHISTLERS_PER_BOX = 5
    CHERIES_BOXES = 1
    CHERIES_SPARKLERS_PER_BOX = 8
    CHERIES_WHISTLERS_PER_BOX = 9

    # Calculate the total number of sparklers and whistlers for Koby
    koby_sparklers = KOBYS_BOXES * KOBYS_SPARKLERS_PER_BOX
    koby_whistlers = KOBYS_BOXES * KOBYS_WHISTLERS_PER_BOX

    # Calculate the total number of sparklers and whistlers for Cherie
    cherie_sparklers = CHERIES_BOXES * CHERIES_SPARKLERS_PER_BOX
    cherie_whistlers = CHERIES_BOXES * CHERIES_WHISTLERS_PER_BOX

    # Calculate the total number of fireworks Koby and Cherie have
    total_sparklers = koby_sparklers + cherie_sparklers
    total_whistlers = koby_whistlers + cherie_whistlers
    total_fireworks = total_sparklers + total_whistlers

    # Display the total number of fireworks
    result = total_fireworks
    return result

print(solution())