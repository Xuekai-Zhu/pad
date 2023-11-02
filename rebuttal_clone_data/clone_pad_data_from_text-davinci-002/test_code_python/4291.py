def solution():
     initial_money = 30
     loan_amount = 15
     interest_rate = 20
     interest_earned = loan_amount * (interest_rate / 100)
     money_after_interest = interest_earned + loan_amount
     lizzy_final_money = initial_money + money_after_interest
     result = lizzy_final_money
     return result

print(solution())