def solution():
    """Mike needed a new pair of jeans. When he got to the mall he saw that his favorite jeans were advertised 25% off. The original price of the jeans was $40. How much money will Mike have left over if he pays with a $50.00 bill?"""
    original_price = 40
    discount_percent = 25
    discount_amount = original_price * (discount_percent / 100)
    sale_price = original_price - discount_amount
    amount_paid = sale_price
    change = 50 - amount_paid
    result = change
    return result

print(solution())