def solution():
    # Calculate the discounted price of the bedroom set
    original_price = 2000
    discount_price = original_price - (original_price * 0.15)  # 15% discount
    credit_card_discount = discount_price - (discount_price * 0.10)  # additional 10% discount with store credit card
    final_price = credit_card_discount - 200  # deduct $200 gift cards
    result = final_price
    return result

print(solution())