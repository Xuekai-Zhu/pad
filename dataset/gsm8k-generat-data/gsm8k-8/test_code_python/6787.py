def solution():
    # Calculate Koby's total sparklers and whistlers
    koby_sparklers = 3 * 2
    koby_whistlers = 5 * 2

    # Calculate Cherie's total sparklers and whistlers
    cherie_sparklers = 8
    cherie_whistlers = 9

    # Calculate the total number of fireworks
    total_sparklers = koby_sparklers + cherie_sparklers
    total_whistlers = koby_whistlers + cherie_whistlers
    total_fireworks = total_sparklers + total_whistlers
    result = total_fireworks
    return result

print(solution())