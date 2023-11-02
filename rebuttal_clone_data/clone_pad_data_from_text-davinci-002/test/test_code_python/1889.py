def solution():
    regular_price = 50
    discount_rate = 40
    discount = regular_price * (discount_rate / 100)
    sale_price = regular_price - discount
    shirts_purchased = 2
    total_price = sale_price * shirts_purchased
    result = total_price
    return result

print(solution())