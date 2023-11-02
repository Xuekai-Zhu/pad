def solution():
     salary = 450
     federal_tax = salary / 3
     state_tax = salary * 0.08
     insurance_payment = 50
     life_insurance_payment = 20
     parking_fee = 10
     final_amount = salary - federal_tax - state_tax - insurance_payment - life_insurance_payment - parking_fee
     result = final_amount
     return result

print(solution())