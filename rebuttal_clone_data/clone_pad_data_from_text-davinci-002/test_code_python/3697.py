def solution():
    winnings = 100
    savings = winnings / 2
    bet = winnings / 2
    profit = bet * 0.6
    savings = (savings + profit) / 2
    result = savings
    return result

print(solution())