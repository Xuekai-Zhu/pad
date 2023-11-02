def solution():
    
    total_coins = 440
    ratio = 10/45 
    amalie_coins = total_coins * (45/55) 
    spent_coins = amalie_coins * (3/4) 
    remaining_coins = amalie_coins - spent_coins
    result = remaining_coins
    return result

print(solution())