def solution():
    original_price = 2000
    gift_cards = 200
    discount_1 = 0.15  # 15% discount
    discount_2 = 0.10  # additional 10% discount with store credit card

    # Calculate the discounted price after the first discount
    first_discounted_price = (1 - discount_1) * (original_price - gift_cards)

    # Calculate the final discounted price after the additional discount with store credit card
    final_discounted_price = (1 - discount_2) * first_discounted_price

    result = final_discounted_price
    return result

print(solution())