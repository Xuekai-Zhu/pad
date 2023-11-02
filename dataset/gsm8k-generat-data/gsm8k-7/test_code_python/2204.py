def solution():
    original_price = 150
    sale_price = 135

    # Calculate the discount amount
    discount = original_price - sale_price

    # Calculate the percentage discount
    percentage_discount = (discount / original_price) * 100
    result = percentage_discount
    return result

print(solution())