def solution():
    """Jed’s family wants to buy 6 different board games. Each board game costs $15 and Jed paid using a $100 bill. If the cashier gave Jed only $5 bills for his change, how many bills did Jed receive?"""
    board_game_cost = 15
    total_cost = board_game_cost * 6
    amount_paid = 100
    change = amount_paid - total_cost
    number_of_bills = change / 5
    result = int(number_of_bills)
    return result

print(solution())