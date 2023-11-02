def solution():
    original_price = 2000  # The original price of the bedroom set is $2000
    gift_card_amount = 200  # Perry has a $200 gift card
    discounted_price = (original_price - gift_card_amount) * 0.85  # 15% discount
    discounted_price_with_card = discounted_price * 0.9  # Additional 10% discount with store credit card
    result = discounted_price_with_card
    return result

print(solution())