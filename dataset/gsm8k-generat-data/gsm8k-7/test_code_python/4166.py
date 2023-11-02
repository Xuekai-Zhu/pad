def solution():
    num_dimes = 10
    num_nickels = 10
    
    # Calculate the value of 10 dimes in pennies
    value_of_dimes = 10 * 10 # 1 dime = 10 pennies
    
    # Calculate the value of 10 nickels in pennies
    value_of_nickels = 10 * 5 # 1 nickel = 5 pennies
    
    # Calculate the total value in pennies
    total_value = value_of_dimes + value_of_nickels
    
    result = total_value
    return result

print(solution())