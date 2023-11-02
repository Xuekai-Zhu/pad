def solution():
    """In a store, an Uno Giant Family Card costs $12. When Ivan bought ten pieces, he was given a discount of $2 each. How much did Ivan pay in all?"""
    card_price = 12
    discount = 2
    discounted_price = card_price - discount
    quantity = 10
    total_cost = quantity * discounted_price
    result = total_cost
    return result

print(solution())