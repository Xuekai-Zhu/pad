def solution():
     original_price = 2000
     discount = 30
     price_after_discount = original_price * (1 - (discount / 100))
     result = price_after_discount
     return result

print(solution())