def solution():
    
    total_coins = 440
    elsa_ratio = 10
    amalie_ratio = 45
    total_ratio = elsa_ratio + amalie_ratio
    amalie_coins = (amalie_ratio / total_ratio) * total_coins
    spent_coins = 0.75 * amalie_coins
    remaining_coins = amalie_coins - spent_coins
    result = remaining_coins
    return result

print(solution())