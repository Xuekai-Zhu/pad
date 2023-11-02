def solution():
    num_pennies = 120
    
    # Calculate the number of nickels by dividing the number of pennies by 3 and then multiplying by 5
    num_nickels = num_pennies // 3 * 5
    
    # Calculate the number of dimes by dividing the number of nickels by 5
    num_dimes = num_nickels // 5
    
    # Calculate the number of quarters by multiplying the number of dimes by 2
    num_quarters = num_dimes * 2
    
    # Calculate the total value of all the coins
    total_value = num_pennies * 0.01 + num_nickels * 0.05 + num_dimes * 0.10 + num_quarters * 0.25
    
    result = total_value
    return result

print(solution())