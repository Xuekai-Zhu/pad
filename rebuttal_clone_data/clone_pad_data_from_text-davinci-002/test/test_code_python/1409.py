def solution():
    prize_money = 100
    percent_given = 20
    money_given = prize_money * (percent_given / 100)
    money_kept = prize_money - money_given
    result = money_kept
    return result

print(solution())