def solution():
    """Bucky earns money each weekend catching and selling fish. He wants to save up for a new video game, which costs $60. Last weekend he earned $35. He can earn $5 from trout and $4 from blue-gill. He caught five fish this Sunday. If 60% were trout, and the rest were blue-gill, how much more does he need to save before he can buy the game?"""
    game_cost = 60
    last_weekend_earnings = 35
    trout_price = 5
    blue_gill_price = 4
    total_fish_caught = 5
    percent_trout = 0.6
    percent_blue_gill = 0.4

    num_trout = total_fish_caught * percent_trout
    num_blue_gill = total_fish_caught * percent_blue_gill

    total_earnings = last_weekend_earnings + (num_trout * trout_price) + (num_blue_gill * blue_gill_price)

    money_needed = game_cost - total_earnings
    result = money_needed
    return result

print(solution())