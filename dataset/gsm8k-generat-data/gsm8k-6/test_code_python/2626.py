def solution():
    slippers_price = 50.00   # price of slippers before discount
    discount = 0.10  # 10% off discount
    discounted_price = slippers_price - (slippers_price * discount)  # price after discount
    embroidery_price = 5.50 * 2  # price for embroidering initials on both shoes
    shipping_price = 10.00  # flat rate shipping cost
    total_price = discounted_price + embroidery_price + shipping_price # total cost of the slippers
    result = total_price
    return result

print(solution())