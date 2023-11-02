def solution():
    """James earns $10 per week as an allowance. After saving all his money for four weeks, he spends half of it on a new video game. He then spends a quarter of what is left to buy a new book. How much money does he have left?"""
    allowance_per_week = 10
    weeks_saved = 4
    total_allowance = allowance_per_week * weeks_saved
    spent_on_video_game = total_allowance / 2
    remaining_money = total_allowance - spent_on_video_game
    spent_on_book = remaining_money / 4
    money_left = remaining_money - spent_on_book
    result = money_left
    return result

print(solution())