def solution():
    """Julia has $40. She spends half of her money to buy a new game for her phone. She spends a quarter of what she has left on in-game purchases. How much money does she have left?"""
    # Initial amount of money
    starting_money = 40

    # Amount spent on the new game
    game_cost = starting_money / 2

    # Amount left after buying the game
    money_left = starting_money - game_cost

    # Amount spent on in-game purchases
    in_game_cost = money_left / 4

    # Amount left after in-game purchases
    money_left -= in_game_cost

    # Display the amount of money Julia has left
    result = money_left
    return result

print(solution())