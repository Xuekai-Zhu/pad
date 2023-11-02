def solution():
     initial_price = 60
     discount_rate = 40
     discount_amount = initial_price * (discount_rate / 100)
     final_price = initial_price - discount_amount
     per_shirt_price = final_price / 3
     result = per_shirt_price
     return result

print(solution())