def solution():
    """Maria's monthly salary is $2000. 20% of her salary goes to paying tax, and 5% goes to insurance. Also, a quarter of the money left after the deductions is spent on utility bills. How much money does Maria have after the deductions and utility bills payment?"""
    # Define Maria's salary
    salary = 2000

    # Calculate the amount of money that goes towards tax and insurance
    tax = salary * 0.2
    insurance = salary * 0.05

    # Calculate the money left after tax and insurance deductions
    remaining_salary = salary - tax - insurance

    # Calculate the money spent on utility bills
    utility_bills = remaining_salary * 0.25

    # Calculate the final amount of money Maria has
    final_amount = remaining_salary - utility_bills

    result = final_amount
    return result

print(solution())