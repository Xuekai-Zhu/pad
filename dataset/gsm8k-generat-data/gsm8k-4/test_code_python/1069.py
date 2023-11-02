def solution():
    """Maria has 4 dimes, 4 quarters, and 7 nickels in her piggy bank. Her mom gives her 5 quarters. How much money, in dollars, does Maria have now?"""
    # Define the value of each coin
    dime_value = 0.1
    quarter_value = 0.25
    nickel_value = 0.05

    # Calculate the total value of the coins Maria had originally
    original_total = (4 * dime_value) + (4 * quarter_value) + (7 * nickel_value)

    # Add the value of the 5 quarters her mom gave her
    new_total = original_total + (5 * quarter_value)

    # Return the result
    result = new_total
    return result

print(solution())