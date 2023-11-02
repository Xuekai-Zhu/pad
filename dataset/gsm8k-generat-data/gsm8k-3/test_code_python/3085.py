def solution():
    """Caden has four jars of coins. One jar of pennies, one jar of nickels, one jar of dimes and one jar of quarters. He has twice as many quarters as he does dimes. He has five times as many nickels as he does dimes. He has three times as many pennies as he does nickels. If he has 120 pennies, how much money does he have?"""
    # Calculate the number of nickels and pennies
    num_pennies = 120
    num_nickels = num_pennies * 3
    # Calculate the number of dimes and quarters
    num_dimes = num_nickels // 5
    num_quarters = num_dimes * 2

    # Calculate the value of each type of coin
    pennies_value = num_pennies * 0.01
    nickels_value = num_nickels * 0.05
    dimes_value = num_dimes * 0.1
    quarters_value = num_quarters * 0.25

    # Calculate the total value of all the coins
    total_value = pennies_value + nickels_value + dimes_value + quarters_value

    # Display the total value
    result = total_value
    return result

print(solution())