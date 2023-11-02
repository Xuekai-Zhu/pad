def solution():
    """Teagan saved 200 pennies in her piggy bank. Rex has a mason jar filled with 100 nickels. Toni has 330 dimes stashed inside a giant mug. How much money did the three kids save altogether?"""
    # Define the values of each coin
    PENNY_VALUE = 0.01
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.1

    # Calculate the total value of Teagan's pennies
    teagan_total = 200 * PENNY_VALUE

    # Calculate the total value of Rex's nickels
    rex_total = 100 * NICKEL_VALUE

    # Calculate the total value of Toni's dimes
    toni_total = 330 * DIME_VALUE

    # Calculate the total amount saved by all three kids
    total_saved = teagan_total + rex_total + toni_total

    # return the result
    result = total_saved
    return result

print(solution())