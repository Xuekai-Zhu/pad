def solution():
    # Calculate the total number of sparklers and whistlers in Koby's boxes
    koby_sparklers = 2 * 3  # 2 boxes, each with 3 sparklers
    koby_whistlers = 2 * 5  # 2 boxes, each with 5 whistlers

    # Calculate the total number of sparklers and whistlers in Cherie's box
    cherie_sparklers = 8  # Cherie's box has 8 sparklers
    cherie_whistlers = 9  # Cherie's box has 9 whistlers

    # Calculate the total number of fireworks
    total_sparklers = koby_sparklers + cherie_sparklers
    total_whistlers = koby_whistlers + cherie_whistlers
    total_fireworks = total_sparklers + total_whistlers
    result = total_fireworks
    return result

print(solution())