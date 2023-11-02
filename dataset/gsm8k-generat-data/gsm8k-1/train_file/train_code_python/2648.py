def solution():
    """In a store, an Uno Giant Family Card costs $12. When Ivan bought ten pieces, he was given a discount of $2 each. How much did Ivan pay in all?"""
    card_cost = 12
    discount_per_card = 2
    num_cards = 10
    total_cost = (card_cost - discount_per_card) * num_cards
    result = total_cost
    return result

print(solution())