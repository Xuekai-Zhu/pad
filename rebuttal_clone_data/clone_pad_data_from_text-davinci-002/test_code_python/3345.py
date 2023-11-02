def solution():
    prize_money = 300
    rica_percent = 3/8
    rica_money = prize_money / rica_percent
    spent_percent = 1/5
    spent_money = rica_money * spent_percent
    result = rica_money + spent_money
    return result

print(solution())