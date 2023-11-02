def solution():
    num_quarters = 76
    num_dimes = 85
    num_nickels = 20
    num_pennies = 150

    # Calculate the total value of all coins in cents
    total_cents = (num_quarters * 25) + (num_dimes * 10) + (num_nickels * 5) + num_pennies

    # Calculate the fee for converting coins to dollars
    conversion_fee = total_cents * 0.1

    # Calculate the total value of all coins in dollars, after the fee
    total_dollars = (total_cents - conversion_fee) / 100
    result = total_dollars
    return result

print(solution())