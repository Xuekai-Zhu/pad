def solution():
     max_amount = 1000
     TV_price = max_amount - 100
     percent_off = 20
     TV_price_discount = TV_price * (percent_off / 100)
     final_TV_price = TV_price - TV_price_discount
     lower_price = max_amount - final_TV_price
     result = lower_price
 
     return result

print(solution())