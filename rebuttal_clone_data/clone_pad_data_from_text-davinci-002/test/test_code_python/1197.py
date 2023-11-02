def solution():
    phone_price_A = 125
    phone_price_B = 130
    discount_A = 8
    discount_B = 10
    final_price_A = phone_price_A - (phone_price_A * (discount_A / 100))
    final_price_B = phone_price_B - (phone_price_B * (discount_B / 100))
    price_difference = final_price_B - final_price_A
    result = price_difference
    return result

print(solution())