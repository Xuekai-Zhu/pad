def solution():
    # Define the values of a dime, nickel, and penny in terms of pennies
    dime_value = 10 * 1
    nickel_value = 5 * 1
    penny_value = 1

    # Convert the 10 dimes and 10 nickels to pennies
    dime_total = 10 * dime_value
    nickel_total = 10 * nickel_value

    # Calculate the total number of pennies
    penny_total = dime_total + nickel_total

    result = penny_total
    return result

print(solution())