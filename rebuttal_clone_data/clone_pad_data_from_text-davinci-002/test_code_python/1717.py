def solution():
     original_price = 40
     discount_percent = 10
     number_of_jeans = 3
     discount_amount = (original_price * discount_percent) / 100
     total_price = (original_price * number_of_jeans) - discount_amount
     result = total_price
     
     return result

print(solution())