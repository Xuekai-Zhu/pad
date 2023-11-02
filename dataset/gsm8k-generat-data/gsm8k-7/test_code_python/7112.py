def solution():
    original_price = 350
    sale_price = 140

    # Calculate the discount amount
    discount = original_price - sale_price

    # Calculate the percentage discount
    percent_off = (discount / original_price) * 100
    result = percent_off
    return result

print(solution())