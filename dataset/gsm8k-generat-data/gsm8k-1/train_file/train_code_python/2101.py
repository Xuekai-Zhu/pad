def solution():
    """Maria's monthly salary is $2000. 20% of her salary goes to paying tax, and 5% goes to insurance. Also, a quarter of the money left after the deductions is spent on utility bills. How much money does Maria have after the deductions and utility bills payment?"""
    salary = 2000
    tax = salary * 0.2
    insurance = salary * 0.05
    remaining_money = salary - tax - insurance
    utility_bills = remaining_money / 4
    final_money = remaining_money - utility_bills
    result = final_money
    return result

print(solution())