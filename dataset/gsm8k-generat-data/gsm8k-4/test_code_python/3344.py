def solution():
    """A jar on the family's counter contains change they've been saving for a trip to the ice cream shop. There are 123 pennies, 85 nickels, 35 dimes, and a number of quarters. All five family members get a double scoop, which costs $3 each. After the trip, they have 48 cents left over. How many quarters were in the jar?"""
    # Define the value of each coin in cents
    PENNY_VALUE = 1
    NICKEL_VALUE = 5
    DIME_VALUE = 10
    QUARTER_VALUE = 25

    # Calculate the total value of all the coins
    total_value = (123 * PENNY_VALUE) + (85 * NICKEL_VALUE) + (35 * DIME_VALUE)

    # Calculate the cost of the ice cream
    ice_cream_cost = 5 * 3 * 100 # Convert $3 to cents and multiply by 5 family members

    # Calculate the remaining change after buying ice cream
    remaining_change = 48

    # Calculate the value of the quarters
    quarters_value = total_value - ice_cream_cost - remaining_change

    # Calculate the number of quarters
    quarters = quarters_value / QUARTER_VALUE

    # return the result
    result = quarters
    return result

print(solution())