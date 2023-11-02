def solution():
    allowance_per_week = 10
    weeks_saved = 4
    total_saved = allowance_per_week * weeks_saved
    video_game_cost = total_saved / 2
    remaining_money = total_saved - video_game_cost
    book_cost = remaining_money / 4
    result = remaining_money - book_cost
    return result

print(solution())