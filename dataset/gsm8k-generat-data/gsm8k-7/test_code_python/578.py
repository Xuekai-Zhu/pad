def solution():
    game_cost = 60
    earned_last_weekend = 35
    trout_price = 5
    bluegill_price = 4
    num_fish_this_weekend = 5
    percentage_trout = 0.6

    # Calculate the total amount earned from this weekend's catch
    num_trout = num_fish_this_weekend * percentage_trout
    num_bluegill = num_fish_this_weekend - num_trout
    total_earned_this_weekend = (num_trout * trout_price) + (num_bluegill * bluegill_price)

    # Calculate the total amount earned so far
    total_earned = earned_last_weekend + total_earned_this_weekend

    # Calculate the amount left to save for the game
    amount_left_to_save = game_cost - total_earned
    result = amount_left_to_save
    return result

print(solution())