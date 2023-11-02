def solution():
    savings_september = 50
    savings_october = 37
    savings_november = 11
    bonus = 25
    video_game_cost = 87

    total_savings = savings_september + savings_october + savings_november

    if total_savings >= 75:
        total_savings += bonus

    remaining_money = total_savings - video_game_cost
    result = remaining_money
    return result

print(solution())