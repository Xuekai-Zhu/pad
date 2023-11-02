def solution():
    # Calculate the total number of sparklers and whistlers in Koby's boxes
    koby_sparklers = 3 * 2  # 2 boxes of sparklers, each containing 3 sparklers
    koby_whistlers = 5 * 2  # 2 boxes of whistlers, each containing 5 whistlers

    # Calculate the total number of sparklers and whistlers in Cherie's box
    cherie_sparklers = 8
    cherie_whistlers = 9

    # Calculate the total number of fireworks
    total_sparklers = koby_sparklers + cherie_sparklers
    total_whistlers = koby_whistlers + cherie_whistlers
    total_fireworks = total_sparklers + total_whistlers

    result = total_fireworks
    return result

print(solution())