def solution():
     pens_purchased = 20
     total_price = 30

     first_10_pens = 10
     second_10_pens = 10

     full_price_pens = first_10_pens
     discount_price_pens = second_10_pens

     full_price = total_price / full_price_pens
     discount_price = full_price / 2

     regular_price = (full_price_pens * full_price + discount_price_pens * discount_price) / pens_purchased

     result = regular_price
     return result

print(solution())