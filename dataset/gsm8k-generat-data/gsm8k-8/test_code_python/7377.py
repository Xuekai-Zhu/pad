def solution():
    # Calculate the total value of Darrel's change in cents
    total_cents = 76 * 25 + 85 * 10 + 20 * 5 + 150

    # Convert the total cents to dollars
    total_dollars = total_cents / 100

    # Calculate the 10% fee
    fee = total_dollars * 0.1

    # Calculate Darrel's total payout after the fee
    payout = total_dollars - fee
    result = payout
    return result

print(solution())