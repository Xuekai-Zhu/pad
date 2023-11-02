def solution():
    """Maria's monthly salary is $2000. 20% of her salary goes to paying tax, and 5% goes to insurance. Also, a quarter of the money left after the deductions is spent on utility bills. How much money does Maria have after the deductions and utility bills payment?"""
    # Define Maria's monthly salary
    salary = 2000

    # Calculate the amount deducted for tax and insurance
    tax = salary * 0.2
    insurance = salary * 0.05
    total_deductions = tax + insurance

    # Calculate the amount left after deducting tax and insurance
    remaining_amount = salary - total_deductions

    # Calculate the amount spent on utility bills
    utility_bills = remaining_amount * 0.25

    # Calculate the amount left after deducting utility bills
    remaining_amount -= utility_bills
    
    # Display the amount left after all deductions and utility bills
    result = remaining_amount
    return result

print(solution())