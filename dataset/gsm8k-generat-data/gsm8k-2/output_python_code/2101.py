def solution():
    """Maria's monthly salary is $2000. 20% of her salary goes to paying tax, and 5% goes to insurance. Also, a quarter of the money left after the deductions is spent on utility bills. How much money does Maria have after the deductions and utility bills payment?"""
    salary = 2000
    tax = 0.2 * salary
    insurance = 0.05 * salary
    remaining_salary = salary - tax - insurance
    utility_bills = 0.25 * remaining_salary
    total_expenses = tax + insurance + utility_bills
    remaining_money = salary - total_expenses
    result = remaining_money
    return result

print(solution())