def solution():
    total_prize_money = 2400
    first_winner_money = total_prize_money / 3  # First winner receives a third of the money
    remaining_money = total_prize_money - first_winner_money
    next_ten_money = remaining_money / 10  # Next ten winners will each receive a tenth of the remaining money
    result = next_ten_money
    return result

print(solution())