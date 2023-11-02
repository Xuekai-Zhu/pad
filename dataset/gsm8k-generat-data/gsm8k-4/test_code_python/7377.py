def solution():
    """Darrel has 76 quarters, 85 dimes, 20 nickels and 150 pennies. If he drops all of his money into a coin-counting machine, they will convert his change into dollars for a 10% fee. How much will he receive after the 10% fee?"""
    # Calculate the total value of Darrel's change in cents
    total_cents = 76 * 25 + 85 * 10 + 20 * 5 + 150

    # Convert the total value into dollars
    total_dollars = total_cents / 100

    # Calculate the 10% fee and subtract it from the total value
    fee = total_dollars * 0.1
    total_dollars -= fee

    # return the result
    result = total_dollars
    return result

print(solution())