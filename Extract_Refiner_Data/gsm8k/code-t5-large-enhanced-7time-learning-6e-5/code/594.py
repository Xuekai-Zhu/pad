def solution():
    
    # Define the value of each type of gumball
    QUARTER_VALUE = 25
    DIME_VALUE = 10
    NICKEL_VALUE = 5
    PENNY_VALUE = 1

    # Define the number of each type of gumball
    num_quarters = 8
    num_dimes = 6
    num_nickels = 14
    num_pennies = 15

    # Calculate the total value of the gumballs
    total_value = (num_quarters * QUARTER_VALUE) + (num_dimes * DIME_VALUE) + (num_nickels * NICKEL_VALUE) + (num_pennies * PENNY_VALUE)

    # Calculate the number of gumballs that can be bought
    num_gumballs = total_value // NICKEL_VALUE

    # Display the number of gumballs that can be bought
    result = num_gumballs
    return result

print(solution())