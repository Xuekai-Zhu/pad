def solution():
    """Jordan is a hockey goalie. In the first period of a game, he blocked four shots. In the second period, he blocked twice as many shots. In the third period, he blocked three fewer than in the second period. When the game ended after the fourth period, he had blocked 21 shots in all. How many did Jordan block in the fourth period?"""
    first_period_blocks = 4
    second_period_blocks = 2 * first_period_blocks
    third_period_blocks = second_period_blocks - 3
    total_blocks = first_period_blocks + second_period_blocks + third_period_blocks + fourth_period_blocks
    fourth_period_blocks = total_blocks - 21
    result = fourth_period_blocks
    return result

print(solution())