def solution():
    """Koby and Cherie want to light fireworks. Koby has bought 2 boxes of fireworks while Cherie has just 1 box of fireworks. Koby’s boxes each contain 3 sparklers and 5 whistlers. Cherie’s box has 8 sparklers and 9 whistlers. In total, how many fireworks do Koby and Cherie have?"""
    koby_sparklers = 2 * 3
    koby_whistlers = 2 * 5
    cherie_sparklers = 8
    cherie_whistlers = 9
    total_sparklers = koby_sparklers + cherie_sparklers
    total_whistlers = koby_whistlers + cherie_whistlers
    total_fireworks = total_sparklers + total_whistlers
    result = total_fireworks
    return result

print(solution())