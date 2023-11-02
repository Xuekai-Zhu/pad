def solution():
    """Teagan saved 200 pennies in her piggy bank.  Rex has a mason jar filled with 100 nickels.  Toni has 330 dimes stashed inside a giant mug.  How much money did the three kids save altogether?"""
    # Define the value of different coins
    PENNY_VALUE = 0.01
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.1

    # Calculate the value of Teagan's pennies
    teagan_pennies = 200
    teagan_value = teagan_pennies * PENNY_VALUE

    # Calculate the value of Rex's nickels
    rex_nickels = 100
    rex_value = rex_nickels * NICKEL_VALUE

    # Calculate the value of Toni's dimes
    toni_dimes = 330
    toni_value = toni_dimes * DIME_VALUE

    # Calculate the total value of all the coins
    total_value = teagan_value + rex_value + toni_value

    # Display the total value
    result = total_value
    return result

print(solution())