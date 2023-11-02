def solution():
    """Tonya is in a hamburger eating contest. Each hamburger is 4 ounces. Last year the winner ate 84 ounces. How many hamburgers does she have to eat to beat last year's winner?"""
    winning_ounces = 84
    hamburger_weight = 4
    hamburgers_to_win = winning_ounces / hamburger_weight
    result = hamburgers_to_win
    return result

print(solution())