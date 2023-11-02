def solution():
    starting_balance = 150.0
    payment = 50.0
    interest_rate = 0.2  # 20% interest

    # Calculate the balance after making the payment
    balance_after_payment = starting_balance - payment

    # Calculate the interest charged on the remaining balance
    interest_charged = interest_rate * balance_after_payment

    # Calculate the new balance after adding the interest
    new_balance = balance_after_payment + interest_charged
    result = new_balance
    return result

print(solution())