def solution():
    """Rocco stores his coins in piles of 10 coins each. He has 4 piles of quarters, 6 piles of dimes, 9 piles of nickels, and 5 piles of pennies. How much money does Rocco have?"""
    # Define the value of each coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Define the number of piles of each coin
    quarter_piles = 4
    dime_piles = 6
    nickel_piles = 9
    penny_piles = 5

    # Calculate the total value of the quarters
    quarter_value = quarter_piles * 10 * QUARTER_VALUE

    # Calculate the total value of the dimes
    dime_value = dime_piles * 10 * DIME_VALUE

    # Calculate the total value of the nickels
    nickel_value = nickel_piles * 10 * NICKEL_VALUE

    # Calculate the total value of the pennies
    penny_value = penny_piles * 10 * PENNY_VALUE

    # Calculate the total value of all the coins
    total_value = (quarter_value + dime_value + nickel_value + penny_value) / 100

    # Display the total value in dollars
    result = total_value
    return result

print(solution())