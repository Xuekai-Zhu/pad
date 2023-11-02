def solution():
    """Koby and Cherie want to light fireworks. Koby has bought 2 boxes of fireworks while Cherie has just 1 box of fireworks. Koby’s boxes each contain 3 sparklers and 5 whistlers. Cherie’s box has 8 sparklers and 9 whistlers. In total, how many fireworks do Koby and Cherie have?"""
    # Define the number of boxes bought by Koby and Cherie
    koby_boxes = 2
    cherie_boxes = 1

    # Define the number of sparklers and whistlers in Koby's boxes
    koby_sparklers = 3 * koby_boxes
    koby_whistlers = 5 * koby_boxes

    # Define the number of sparklers and whistlers in Cherie's box
    cherie_sparklers = 8
    cherie_whistlers = 9

    # Calculate the total number of sparklers and whistlers
    total_sparklers = koby_sparklers + cherie_sparklers
    total_whistlers = koby_whistlers + cherie_whistlers

    # Calculate the total number of fireworks
    total_fireworks = total_sparklers + total_whistlers

    # return the result
    result = total_fireworks
    return result

print(solution())