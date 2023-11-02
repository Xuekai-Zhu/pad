def solution():
    """Caden has four jars of coins. One jar of pennies, one jar of nickels, one jar of dimes and one jar of quarters. He has twice as many quarters as he does dimes. He has five times as many nickels as he does dimes. He has three times as many pennies as he does nickels. If he has 120 pennies, how much money does he have?"""
    # Define the number of pennies and the conversion factors
    num_pennies = 120
    penny_value = 0.01
    nickel_value = 0.05
    dime_value = 0.1
    quarter_value = 0.25

    # Calculate the number of nickels 
    num_nickels = num_pennies // 3
    # Calculate the value of the nickels 
    value_nickels = num_nickels * nickel_value

    # Calculate the number of dimes 
    num_dimes = num_nickels // 5
    # Calculate the value of the dimes 
    value_dimes = num_dimes * dime_value

    # Calculate the number of quarters 
    num_quarters = num_dimes * 2
    # Calculate the value of the quarters 
    value_quarters = num_quarters * quarter_value

    # Calculate the total value of the coins 
    total_value = value_nickels + value_dimes + value_quarters + (num_pennies * penny_value)

    result = total_value
    return result

print(solution())