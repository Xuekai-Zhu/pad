def solution():
    """Jed’s family wants to buy 6 different board games. Each board game costs $15 and Jed paid using a $100 bill. If the cashier gave Jed only $5 bills for his change, how many bills did Jed receive?"""
    cost_per_game = 15
    num_games = 6
    total_cost = cost_per_game * num_games
    payment = 100
    change = payment - total_cost
    num_bills = change // 5
    result = num_bills
    return result

print(solution())