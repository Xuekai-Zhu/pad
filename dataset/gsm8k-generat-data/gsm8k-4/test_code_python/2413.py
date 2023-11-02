def solution():
    """Val has three times as many dimes as nickels. If she accidentally finds twice as many nickels as she has in her older brother's treasure box, and takes them for herself, what would be the value of money she has, in dollars, if she had 20 nickels before finding the new ones from her brother's treasure box?"""
    # Define the number of nickels Val had initially
    initial_nickels = 20

    # Define the ratio of dimes to nickels
    dime_to_nickel_ratio = 3

    # Calculate the number of dimes based on the ratio
    initial_dimes = dime_to_nickel_ratio * initial_nickels

    # Calculate the total value of the initial coins
    initial_value = (0.05 * initial_nickels) + (0.10 * initial_dimes)

    # Calculate the number of new nickels found in the treasure box
    new_nickels = 2 * initial_nickels

    # Calculate the total value of the new coins
    new_value = 0.05 * new_nickels

    # Calculate the final total value of all the coins
    final_value = initial_value + new_value

    # Format the final value as a dollar amount
    result = "${:.2f}".format(final_value)
    return result

print(solution())