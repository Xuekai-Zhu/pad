def solution():
    """George wants to borrow $100 from a loan shark. The finance fee starts at 5% and doubles every week. If George plans to borrow for 2 weeks, how much in fees will he have to pay?"""
    # Define the initial loan amount and finance fee
    loan_amount = 100
    finance_fee = 0.05

    # Calculate the finance fee for the first week
    week1_fee = loan_amount * finance_fee

    # Double the finance fee for the second week
    finance_fee *= 2

    # Calculate the finance fee for the second week
    week2_fee = loan_amount * finance_fee

    # Calculate the total fees George will have to pay
    total_fees = week1_fee + week2_fee

    # Display the total fees
    result = total_fees
    return result

print(solution())