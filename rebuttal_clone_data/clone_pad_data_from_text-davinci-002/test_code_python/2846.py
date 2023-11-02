def solution():
    game_cost = 60
    candy_cost = 5
    babysitting_rate = 8
    hours_worked = 9
    total_money_earned = hours_worked * babysitting_rate
    total_money_spent = game_cost + candy_cost
    money_left_over = total_money_earned - total_money_spent
    result = money_left_over
    return result

print(solution())