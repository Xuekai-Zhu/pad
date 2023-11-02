def solution():
    prize_money = 2400
    first_prize = prize_money / 3
    remaining_money = prize_money - first_prize
    prize_per_winner = remaining_money / 10
    result = prize_per_winner
    
    return result

print(solution())