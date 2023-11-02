def solution():
    """Perry wants to buy a new modern bedroom set for $2000. He received $200.00 in gift cards over the holidays that he can use toward the set. The store is currently offering the entire set at 15% off. If he signs up for the store credit card and uses it to buy the set, he will save an additional 10% off on the discounted set. What is the final price of the set?"""
    set_price = 2000
    gift_cards = 200
    discounted_price = set_price * 0.85
    credit_card_discount = discounted_price * 0.1
    final_price = discounted_price - credit_card_discount - gift_cards
    result = final_price
    return result

print(solution())