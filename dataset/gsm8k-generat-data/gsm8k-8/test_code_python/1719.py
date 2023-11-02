def solution():
    # Define the initial balance and payment
    balance = 150.00
    payment = 50.00

    # Calculate the remaining balance after the payment
    remaining_balance = balance - payment

    # If there is still a remaining balance, apply the interest
    if remaining_balance > 0:
        interest = remaining_balance * 0.20
        remaining_balance += interest

    result = remaining_balance
    return result

print(solution())