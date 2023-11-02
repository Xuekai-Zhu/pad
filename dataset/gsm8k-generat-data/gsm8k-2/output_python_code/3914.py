def solution():
    """Jordan is a hockey goalie. In the first period of a game, he blocked four shots. In the second period, he blocked twice as many shots. In the third period, he blocked three fewer than in the second period. When the game ended after the fourth period, he had blocked 21 shots in all. How many did Jordan block in the fourth period?"""
    period_1 = 4
    period_2 = 2 * period_1
    period_3 = period_2 - 3
    total_shots = 21
    shots_in_period_4 = total_shots - period_1 - period_2 - period_3
    result = shots_in_period_4
    return result

print(solution())