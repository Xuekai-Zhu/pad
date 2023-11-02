def solution():
    """A jar on the family's counter contains change they've been saving a trip to the ice cream shop. There are 123 pennies, 85 nickels, 35 dimes, and a number of quarters. All five family members get a double scoop, which costs $3 each. After the trip, they have 48 cents left over. How many quarters were in the jar?"""
    # Define the value of each coin in cents
    PENNY_VALUE = 1
    NICKEL_VALUE = 5
    DIME_VALUE = 10
    QUARTER_VALUE = 25

    # Calculate the total value of each type of coin
    total_pennies = PENNY_VALUE * 123
    total_nickels = NICKEL_VALUE * 85
    total_dimes = DIME_VALUE * 35

    # Calculate the total value of all the coins
    total_value = total_pennies + total_nickels + total_dimes + (QUARTER_VALUE * x)

    # Calculate the total cost of the ice cream
    total_cost = 3 * 5

    # Calculate the remaining change
    remaining_change = total_value - total_cost - 48

    # Calculate the number of quarters based on the remaining change
    x = remaining_change // QUARTER_VALUE

    # Display the number of quarters
    result = x
    return result

print(solution())