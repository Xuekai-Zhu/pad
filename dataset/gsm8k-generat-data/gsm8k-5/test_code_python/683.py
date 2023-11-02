def solution():
    money_start = 40  # Julia starts with $40
    money_after_game = money_start / 2  # Julia spends half of her money on the game
    money_left = money_start - money_after_game  # Julia has this much money left after buying the game
    money_spent_on_in_game_purchases = money_left / 4  # Julia spends a quarter of what she has left on in-game purchase
    money_remaining = money_left - money_spent_on_in_game_purchases  # Julia has this much money remaining
    result = money_remaining
    return result

print(solution())