def solution():
    # Calculate the new balance after making a $50.00 payment
    starting_balance = 150.00
    payment = 50.00
    remaining_balance = starting_balance - payment

    # Calculate the interest charged if there is a remaining balance
    if remaining_balance > 0:
        interest = 0.20 * remaining_balance
        new_balance = remaining_balance + interest
    else:
        new_balance = remaining_balance

    result = new_balance
    return result

print(solution())