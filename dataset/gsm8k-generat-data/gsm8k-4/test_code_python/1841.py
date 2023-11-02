def solution():
    """Mac loves the shape of quarters and is willing to trade money for them, even if he loses value. He tells his brother that he will trade him 3 dimes for a quarter or 7 nickels. He trades for 20 quarters with dimes and 20 quarters with nickels. How many dollars did Mac lose?"""
    
    # Define the value of a quarter, dime, and nickel
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.1
    NICKEL_VALUE = 0.05

    # Calculate the number of quarters Mac gets from trading 20 times with dimes
    quarters_from_dimes = 20 * 3

    # Calculate the number of dimes needed to trade for 20 quarters
    dimes_for_quarters = 20 / 3

    # Calculate the number of quarters Mac gets from trading 20 times with nickels
    quarters_from_nickels = 20 * 7

    # Calculate the number of nickels needed to trade for 20 quarters
    nickels_for_quarters = 20 / 7

    # Calculate the total value of the quarters obtained by trading with dimes
    dimes_value = dimes_for_quarters * DIME_VALUE
    quarters_value_from_dimes = quarters_from_dimes * QUARTER_VALUE
    total_value_from_dimes = quarters_value_from_dimes - dimes_value

    # Calculate the total value of the quarters obtained by trading with nickels
    nickels_value = nickels_for_quarters * NICKEL_VALUE
    quarters_value_from_nickels = quarters_from_nickels * QUARTER_VALUE
    total_value_from_nickels = quarters_value_from_nickels - nickels_value

    # Calculate the total amount of money Mac lost
    total_loss = total_value_from_dimes + total_value_from_nickels - 10

    # return the result
    result = total_loss
    return result

print(solution())