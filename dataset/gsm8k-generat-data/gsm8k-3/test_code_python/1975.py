def solution():
    """Tony puts $1,000 in a savings account for 1 year. It earns 20% interest. He then takes out half the money to buy a new TV. The next year, the remaining money earns 15% interest. How much is now in the account?"""
    # Calculate the interest earned in the first year
    interest_1 = 1000 * 0.2

    # Calculate the total amount in the account after the first year
    total_1 = 1000 + interest_1

    # Take out half the money to buy a new TV
    total_2 = total_1 / 2

    # Calculate the interest earned in the second year
    interest_2 = total_2 * 0.15

    # Calculate the total amount in the account after the second year
    total_3 = total_2 + interest_2

    # Display the total amount in the account
    result = total_3
    return result

print(solution())