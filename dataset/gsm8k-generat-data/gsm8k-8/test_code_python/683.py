def solution():
    # Define Julia's starting amount of money
    initial_money = 40

    # Calculate half of her money
    half_money = initial_money / 2

    # Calculate the remaining amount of money
    remaining_money = initial_money - half_money

    # Calculate a quarter of the remaining amount of money
    in_game_purchases = remaining_money / 4

    # Calculate Julia's final amount of money
    final_money = remaining_money - in_game_purchases
    result = final_money
    return result

print(solution())