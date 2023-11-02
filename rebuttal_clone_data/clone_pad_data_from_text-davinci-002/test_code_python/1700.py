def solution():
     purchase_price = 35000
     loan_amount = 20000
     interest_rate = 15
     total_amount = purchase_price + loan_amount + (loan_amount * (interest_rate/100))
     result = total_amount
     return result

print(solution())