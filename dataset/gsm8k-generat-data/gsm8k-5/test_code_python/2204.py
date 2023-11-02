def solution():
    original_price = 150  # The original price of the bag
    sale_price = 135  # The sale price of the bag
    discount = original_price - sale_price  # The discount
    percent_discount = (discount / original_price) * 100  # The percent discount

    result = percent_discount
    return result

print(solution())