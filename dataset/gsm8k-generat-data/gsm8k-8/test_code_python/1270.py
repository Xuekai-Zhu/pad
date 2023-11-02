def solution():
    # Define the total cost of the house and the deposit paid
    total_cost = 280
    deposit = 40

    # Calculate the remaining balance to be paid
    remaining_balance = total_cost - deposit

    # Calculate the total number of months over 10 years
    total_months = 10 * 12

    # Calculate the monthly payment needed to pay off the remaining balance in 10 years
    monthly_payment = remaining_balance / total_months

    result = monthly_payment
    return result

print(solution())