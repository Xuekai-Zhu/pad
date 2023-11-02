def solution():
    """Cindy tosses 5 dimes into the wishing pond. Eric flips 3 quarters into the pond. Garrick throws in 8 nickels. Ivy then drops 60 pennies in. If Eric dips his hands into the water and pulls out a quarter, how much money, in cents, did they put into the pond?"""
    # Define the values of the coins
    dime_value = 10
    quarter_value = 25
    nickel_value = 5
    penny_value = 1

    # Calculate the total value of the coins tossed in the pond
    total_value = (5 * dime_value) + (3 * quarter_value) + (8 * nickel_value) + (60 * penny_value)

    result = total_value
    return result

print(solution())