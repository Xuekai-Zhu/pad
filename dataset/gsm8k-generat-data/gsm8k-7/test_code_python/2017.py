def solution():
    num_board_games = 6
    price_per_game = 15
    payment = 100

    # Calculate the total cost of all board games
    total_cost = num_board_games * price_per_game

    # Calculate the change that Jed should receive
    change = payment - total_cost

    # Calculate the number of $5 bills in the change
    num_fives = change // 5

    result = num_fives
    return result

print(solution())