def solution():
    """Tyrone empties his piggy bank and finds two $1 bills, a $5 bill, 13 quarters, 20 dimes, 8 nickels, and 35 pennies. How much money does Tyrone have?"""
    # Define the value of each coin and bill
    dollar_value = 1
    five_dollar_value = 5
    quarter_value = 0.25
    dime_value = 0.1
    nickel_value = 0.05
    penny_value = 0.01

    # Calculate the total value of each type of coin and bill
    total_dollars = 2 * dollar_value + five_dollar_value
    total_quarters = 13 * quarter_value
    total_dimes = 20 * dime_value
    total_nickels = 8 * nickel_value
    total_pennies = 35 * penny_value

    # Calculate the total value of all the coins and bills
    total_value = total_dollars + total_quarters + total_dimes + total_nickels + total_pennies

    # return the result
    result = round(total_value,2)
    return result

print(solution())