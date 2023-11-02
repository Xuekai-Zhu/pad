def solution():
    """Michael buys his suit for $430 and shoes for $190. So, if he gets a $100 discount, what was the amount that he paid to the seller?"""
    suit_price = 430
    shoes_price = 190
    discount = 100
    total_price = suit_price + shoes_price
    total_price -= discount
    result = total_price
    return result

print(solution())