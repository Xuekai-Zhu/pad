def solution():
    balance = 50.00  # Chip has a $50.00 balance on his credit card
    interest_rate = 0.20  # Chip will be charged a 20% interest fee

    # Calculate the balance after the first interest fee
    balance += balance * interest_rate

    # Add the $20.00 charge to the balance
    balance += 20.00

    # Calculate the balance after the second interest fee
    balance += balance * interest_rate

    result = balance
    return result

print(solution())