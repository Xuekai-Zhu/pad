def solution():
    """Charlotte needs to know how much money to have with her when she goes to the shoe store. How much money should Charlotte bring to buy a pair of boots, if the original price is $90 and there is a discount of 20%?"""
    original_price = 90
    discount_percentage = 20
    discount_amount = original_price * (discount_percentage / 100)
    sale_price = original_price - discount_amount
    result = sale_price
    return result

print(solution())