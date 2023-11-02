def solution():
     mango_juice_price = 5
     pineapple_juice_price = 6
     total_price = 94
     pineapple_juice_total = 54
     mango_juice_total = total_price - pineapple_juice_total
     mango_juice_people = mango_juice_total / mango_juice_price
     pineapple_juice_people = pineapple_juice_total / pineapple_juice_price
     total_people = mango_juice_people + pineapple_juice_people
     result = total_people
     return result

print(solution())