def solution():
    
    # Define the value of each coin in cents
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Define the number of each coin in cents
    quarter_count = 32
    dime_count = 95
    nickel_count = 120
    penny_count = 750

    # Calculate the total value of the quarters
    quarter_value = quarter_count * QUARTER_VALUE

    # Calculate the total value of the dimes
    dime_value = dime_count * DIME_VALUE

    # Calculate the total value of the nickels
    nickel_value = nickel_count * NICKEL_VALUE

    # Calculate the total value of the pennies
    penny_value = penny_count * PENNY_VALUE

    # Calculate the total value of the coins in the jar
    total_value = quarter_value + dime_value + nickel_value + penny_value

print(solution())