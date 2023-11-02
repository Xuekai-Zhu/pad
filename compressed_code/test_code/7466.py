def solution():
    
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