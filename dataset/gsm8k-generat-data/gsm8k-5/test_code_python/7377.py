def solution():
    # Calculate the total value of Darrel's change in cents
    total_cents = 76 * 25 + 85 * 10 + 20 * 5 + 150 * 1

    # Convert the total value to dollars
    total_dollars = total_cents / 100

    # Calculate the 10% fee and subtract it from the total dollars
    fee = total_dollars * 0.1
    money_received = total_dollars - fee
    result = money_received
    return result

print(solution())