def solution():
    """Percy wants to save up for a new PlayStation, which costs $500. He gets $200 on his birthday and $150 at Christmas. To make the rest of the money, he's going to sell his old PlayStation games for $7.5 each. How many games does he need to sell to reach his goal?"""
    target_amount = 500
    savings = 200 + 150
    remaining_amount = target_amount - savings
    game_price = 7.5
    games_needed = remaining_amount / game_price
    result = games_needed
    
    return result

print(solution())