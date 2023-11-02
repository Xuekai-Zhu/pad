def solution():
    """Jed’s family wants to buy 6 different board games. Each board game costs $15 and Jed paid using a $100 bill. If the cashier gave Jed only $5 bills for his change, how many bills did Jed receive?"""
    # Define the cost of each board game and the amount paid by Jed
    BOARD_GAME_COST = 15
    PAID_AMOUNT = 100

    # Calculate the total cost of the board games
    total_cost = 6 * BOARD_GAME_COST

    # Calculate the amount of change Jed should receive
    change_amount = PAID_AMOUNT - total_cost

    # Calculate the number of $5 bills Jed should receive
    num_bills = change_amount // 5

    # Display the number of $5 bills Jed received
    result = num_bills
    return result

print(solution())