def solution():
    cost_of_board_game = 15  # Each board game costs $15
    number_of_board_games = 6  # Jed’s family wants to buy 6 different board games
    total_cost = cost_of_board_game * number_of_board_games  # Total cost of 6 board games
    amount_paid = 100  # Jed paid using a $100 bill
    change = amount_paid - total_cost  # Calculate the change

    # Calculate the number of $5 bills Jed received
    num_of_5_dollar_bills = change // 5
    result = num_of_5_dollar_bills
    return result

print(solution())