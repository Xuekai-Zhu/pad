def solution():
    shirts_purchased = 3
    shirt_price = 10
    percent_discount_2 = 50
    percent_discount_3 = 60
    discount_2 = shirt_price * (percent_discount_2 / 100)
    discount_3 = shirt_price * (percent_discount_3 / 100)
    total_ discount = discount_2 + discount_3
    total_price = shirt_price * shirts_purchased
    final_price = total_price - total_discount
    result = final_price
    return result

print(solution())