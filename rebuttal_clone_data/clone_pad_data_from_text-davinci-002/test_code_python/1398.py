def solution(): 
 original_price = 90
 discount = 20
 sale_price = original_price * (1 - (discount/100))
 result = sale_price

 return result

print(solution())