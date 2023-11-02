def solution():
    """Jack and Jill are friends who borrow from each other often. Last week Jack borrowed  $1200 from Jill, which he promised to pay back with an interest of 10%. How much will Jack pay back?"""
    # Define the initial loan amount and the interest rate
    loan_amount = 1200
    interest_rate = 0.1

    # Calculate the interest amount
    interest_amount = loan_amount * interest_rate

    # Calculate the total amount to be paid back
    total_amount = loan_amount + interest_amount
    
    result = total_amount
    return result

print(solution())