def solution():
    borrowed_amount = 100  # George wants to borrow $100
    finance_fee = 0.05  # The finance fee starts at 5%
    total_finance_fee = 0  # Initialize the total finance fee

    # Calculate the total finance fee for 2 weeks
    for week in range(1, 3):
        total_finance_fee += borrowed_amount * finance_fee
        finance_fee *= 2  # Double the finance fee every week

    result = total_finance_fee
    return result

print(solution())