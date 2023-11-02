def solution():
    """Darrel has 76 quarters, 85 dimes, 20 nickels and 150 pennies.  If he drops all of his money into a coin-counting machine, they will convert his change into dollars for a 10% fee.  How much will he receive after the 10% fee?"""
    # Define the value of each type of coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Calculate the total value of Darrel's change in cents
    total_value = (76 * QUARTER_VALUE) + (85 * DIME_VALUE) + (20 * NICKEL_VALUE) + (150 * PENNY_VALUE)

    # Calculate the fee for converting the change into dollars
    fee = total_value * 0.1

    # Calculate the total amount Darrel will receive after the fee
    total_amount = (total_value - fee) / 100

    # Display the total amount Darrel will receive
    result = total_amount
    return result

print(solution())