def solution():
    
    total_piles = 10
    piles_x = 6
    piles_y = total_piles - piles_x
    hands_x = 9
    hands_y = 12
    bananas_x = 14
    bananas_y = 9
    total_bananas_x = piles_x * hands_x * bananas_x
    total_bananas_y = piles_y * hands_y * bananas_y
    total_bananas = total_bananas_x + total_bananas_y
    result = total_bananas / 12
    return result

print(solution())