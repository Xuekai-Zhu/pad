def solution():
    """Erwan went on shopping. He purchased a pair of shoes at $200 but discounted 30%, and two shirts at $80 each. Upon checkout, the cashier said that there is an additional 5% discount. How much did he spend after all the discounts?"""
    # Define the initial prices of the shoes and shirts
    shoes_price = 200
    shirt_price = 80

    # Calculate the discounted price of the shoes
    shoes_discount = shoes_price * 0.3
    shoes_discounted_price = shoes_price - shoes_discount

    # Calculate the total price of the shirts
    shirts_price = shirt_price * 2

    # Calculate the total price before the additional discount
    total_price_before_discount = shoes_discounted_price + shirts_price

    # Calculate the additional discount
    additional_discount = total_price_before_discount * 0.05

    # Calculate the total price after all the discounts
    total_price_after_discount = total_price_before_discount - additional_discount

    result = total_price_after_discount
    return result

print(solution())