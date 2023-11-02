def solution():
    total_prize_money = 2400
    
    # Calculate the amount won by the first winner
    first_winner_winnings = total_prize_money / 3
    
    # Calculate the remaining prize money
    remaining_prize_money = total_prize_money - first_winner_winnings
    
    # Calculate the amount won by each of the next 10 winners
    next_10_winner_winnings = remaining_prize_money / 10
    
    result = next_10_winner_winnings
    return result

print(solution())