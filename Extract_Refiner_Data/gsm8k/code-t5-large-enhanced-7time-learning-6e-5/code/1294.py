def solution():
    
    # Define the value of each coin in cents
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1

    # Calculate the total value of the quarters in cents
    quarter_total = 32 * quarter_value

    # Calculate the total value of the dimes in cents
    dime_total = 95 * dime_value

    # Calculate the total value of the nickels in cents
    nickel_total = 120 * nickel_value

    # Calculate the total value of the pennies in cents
    penny_total = 750 * penny_value

    # Calculate the total value in dollars in the jar
    total_value = quarter_total + dime_total + nickel_total + penny_total

    # return the result
    result = total_value
    return result

print(solution())