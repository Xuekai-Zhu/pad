def solution():
    """Tonya is in a hamburger eating contest. Each hamburger is 4 ounces. Last year the winner ate 84 ounces. How many hamburgers does she have to eat to beat last year's winner?"""
    ounces_per_hamburger = 4
    ounces_to_beat = 84
    hamburgers_to_beat = ounces_to_beat / ounces_per_hamburger
    result = hamburgers_to_beat
    return result

print(solution())