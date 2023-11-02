def solution():
     monthly_payment = 100
     interest_rate = 0.1
     total_payment = monthly_payment * 12
     total_interest = total_payment * interest_rate
     final_payment = total_payment + total_interest
     result = final_payment
     return result

print(solution())