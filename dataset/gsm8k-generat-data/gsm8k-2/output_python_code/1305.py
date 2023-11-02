def solution():
    """Anna's mom gave her $10.00 to buy anything she wanted from the candy store. Anna bought 3 packs of chewing gum for $1.00 each, 5 chocolate bars at $1 each and 2 large candy canes for $0.50 each. How much money did Anna have left?"""
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