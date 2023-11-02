def solution():
     TV_price = 480
     discount_percent = 5
     down_payment = 150
     monthly_installments = 3
     TV_price_discount = TV_price * (discount_percent / 100) 
     TV_price_final = TV_price - TV_price_discount
     monthly_payment = (TV_price_final - down_payment) / monthly_installments
     result = monthly_payment
     
     return result

print(solution())