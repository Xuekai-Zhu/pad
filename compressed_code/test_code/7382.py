def solution():
    
    cost_per_game = 15
    num_games = 6
    total_cost = cost_per_game * num_games
    payment = 100
    change = payment - total_cost
    num_bills = change // 5
    result = num_bills
    return result

print(solution())