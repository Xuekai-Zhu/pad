def solution():
    """George wants to borrow $100 from a loan shark. The finance fee starts at 5% and doubles every week. If George plans to borrow for 2 weeks, how much in fees will he have to pay?"""
    # Define the initial loan amount and the number of weeks
    loan_amount = 100
    weeks = 2

    # Define the initial finance fee rate
    finance_rate = 0.05

    # Calculate the total finance fees for the two weeks
    total_fees = 0
    for i in range(weeks):
        # Calculate the finance fee for the current week and add it to the total
        current_fee = loan_amount * finance_rate
        total_fees += current_fee
        
        # Double the finance rate for the next week
        finance_rate *= 2

    result = total_fees
    return result

print(solution())