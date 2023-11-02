def solution():
    
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