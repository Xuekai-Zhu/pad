def solution():
    
    prize_money = 2400
    first_winner_money = prize_money / 3
    remaining_money = prize_money - first_winner_money
    next_winners_money = remaining_money / 10
    result = next_winners_money
    return result

print(solution())