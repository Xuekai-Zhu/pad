def solution():
    """A family of 12 monkeys collected 10 piles of bananas. 6 piles had 9 hands, with each hand having 14 bananas, while the remaining piles had 12 hands, with each hand having 9 bananas. How many bananas would each monkey get if they divide the bananas equally amongst themselves?"""
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