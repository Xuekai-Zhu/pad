def solution():
    sale_price = 450  # Solomon paid $450 after a 10% discount
    discount_percentage = 10  # Solomon got a 10% discount on the dining table
    original_price = sale_price / (1 - (discount_percentage / 100))  # Calculate the original price using the sale price and discount percentage
    result = original_price
    return result

print(solution())