def solution():
    
    target_amount = 500
    savings = 200 + 150
    remaining_amount = target_amount - savings
    game_price = 7.5
    games_needed = remaining_amount / game_price
    result = games_needed
    
    return result

print(solution())