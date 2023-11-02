def solution():
    
    winnings = 100
    percent_given_away = 20
    amount_given_away = winnings * (percent_given_away / 100)
    amount_kept = winnings - amount_given_away
    result = amount_kept
    return result

print(solution())