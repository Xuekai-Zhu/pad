def solution():
    """Rocco stores his coins in piles of 10 coins each. He has 4 piles of quarters, 6 piles of dimes, 9 piles of nickels, and 5 piles of pennies. How much money does Rocco have?"""
    # Define the value of each coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the value of each type of coin
    quarter_total = 4 * 10 * quarter_value
    dime_total = 6 * 10 * dime_value
    nickel_total = 9 * 10 * nickel_value
    penny_total = 5 * 10 * penny_value

    # Calculate the total value of all the coins
    total_value = quarter_total + dime_total + nickel_total + penny_total

    # Return the result
    result = total_value
    return result

print(solution())