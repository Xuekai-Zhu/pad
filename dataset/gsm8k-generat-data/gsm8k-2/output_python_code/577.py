def solution():
    """Bucky earns money each weekend catching and selling fish. He wants to save up for a new video game, which costs $60. Last weekend he earned $35. He can earn $5 from trout and $4 from blue-gill. He caught five fish this Sunday. If 60% were trout, and the rest were blue-gill, how much more does he need to save before he can buy the game?"""
    game_cost = 60
    last_weekend_earnings = 35
    trout_price = 5
    bluegill_price = 4
    total_fish_caught = 5
    trout_ratio = 0.6
    num_trout = int(total_fish_caught * trout_ratio)
    num_bluegill = total_fish_caught - num_trout
    earnings_from_trout = num_trout * trout_price
    earnings_from_bluegill = num_bluegill * bluegill_price
    total_earnings = last_weekend_earnings + earnings_from_trout + earnings_from_bluegill
    remaining_cost = game_cost - total_earnings
    result = remaining_cost
    return result

print(solution())