def solution():
    """Julia has $40. She spends half of her money to buy a new game for her phone. She spends a quarter of what she has left on in-game purchases. How much money does she have left?"""
    # Define the initial amount of money
    initial_money = 40

    # Calculate the amount spent on the new game
    game_cost = initial_money / 2

    # Calculate the amount of money left after buying the game
    left_money = initial_money - game_cost

    # Calculate the amount spent on in-game purchases
    in_game_purchases_cost = left_money / 4

    # Calculate the amount of money left after in-game purchases
    money_left = left_money - in_game_purchases_cost

    result = money_left
    return result

print(solution())