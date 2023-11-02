def solution():
    
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