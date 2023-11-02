def solution():
    # Define initial amount and loaned amount
    initial_amount = 30
    loaned_amount = 15

    # Find out how much interest is earned
    interest = 0.2 * loaned_amount

    # Add interest to the loaned amount to get total repayment
    total_repayment = loaned_amount + interest

    # Subtract the total repayment from the initial amount to get the final amount
    final_amount = initial_amount - total_repayment
    result = final_amount
    return result

print(solution())