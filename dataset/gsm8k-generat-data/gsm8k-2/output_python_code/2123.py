def solution():
    """James earns $10 per week as an allowance. After saving all his money for four weeks, he spends half of it on a new video game. He then spends a quarter of what is left to buy a new book. How much money does he have left?"""
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