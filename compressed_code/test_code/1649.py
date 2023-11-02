def solution():
    
    weekly_allowance = 10
    num_weeks_saved = 4
    total_savings = weekly_allowance * num_weeks_saved
    half_for_game = total_savings / 2
    remaining_money = total_savings - half_for_game
    quarter_for_book = remaining_money / 4
    money_left = remaining_money - quarter_for_book
    result = money_left
    return result

print(solution())