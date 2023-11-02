def solution():
    """Vanessa has decided to sell some of her clothes to make pocket money, offering a standard price for each type of item. She made a total of $69 by selling 7 dresses and 4 shirts. If she managed to sell each shirt for $5, how much did the dresses sell for each?"""
    total_items = 11
    total_amount = 69
    shirts = 4
    shirt_price = 5
    dress_price = (total_amount - (shirts * shirt_price)) / (total_items - shirts)
    result = dress_price
    return result

print(solution())