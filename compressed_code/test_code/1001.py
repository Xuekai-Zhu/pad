def solution():
    
    gum_price = 1
    gum_packs = 3
    chocolate_price = 1
    chocolate_bars = 5
    candy_cane_price = 0.5
    candy_canes = 2
    total_spent = gum_price * gum_packs + chocolate_price * chocolate_bars + candy_cane_price * candy_canes
    money_left = 10 - total_spent
    result = money_left
    return result

print(solution())