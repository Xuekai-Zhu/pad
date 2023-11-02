def solution():
    """Todd bought a pair of jeans that cost $125 at full price. The jeans were on sale for 20% off. He then applied a coupon that took off $10. He paid with a store credit card that gave him another 10% off the remaining amount. How many dollars did he save on the original price of the jeans?"""
    # Define the original price of the jeans and the discount percentages
    original_price = 125
    sale_discount = 0.2
    coupon_discount = 10
    card_discount = 0.1

    # Calculate the price after each discount
    price_after_sale = original_price * (1 - sale_discount)
    price_after_coupon = price_after_sale - coupon_discount
    price_after_card = price_after_coupon * (1 - card_discount)

    # Calculate the amount saved on the original price
    amount_saved = original_price - price_after_card

    # Display the amount saved
    result = amount_saved
    return result

print(solution())