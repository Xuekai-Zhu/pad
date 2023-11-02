def solution():
    # Define the initial debt
    initial_debt = 40

    # Calculate the amount paid back
    amount_paid_back = initial_debt / 2

    # Calculate the new debt after the payment
    new_debt = initial_debt - amount_paid_back

    # Add the new borrowing
    new_borrowing = 10
    total_debt = new_debt + new_borrowing

    result = total_debt
    return result

print(solution())