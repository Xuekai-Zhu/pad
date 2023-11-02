def solution():
    """Val has three times as many dimes as nickels. If she accidentally finds twice as many nickels as she has in her older brother's treasure box, and takes them for herself, what would be the value of money she has, in dollars, if she had 20 nickels before finding the new ones from her brother's treasure box?"""
    # Define the value of a nickel and a dime
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.1

    # Calculate the number of nickels Val originally had
    original_nickels = 20

    # Calculate the number of nickels she found in her brother's treasure box
    new_nickels = 2 * original_nickels

    # Calculate the total number of nickels
    total_nickels = original_nickels + new_nickels

    # Calculate the number of dimes Val has
    dimes = 3 * total_nickels

    # Calculate the total value of all the coins
    total_value = (total_nickels * NICKEL_VALUE) + (dimes * DIME_VALUE)

    # Display the total value in dollars
    result = total_value
    return result

print(solution())