def solution():
    # Define the number of nickels and dimes Val had before finding her brother's treasure box
    num_nickels = 20
    num_dimes = 3 * num_nickels

    # Find the number of nickels Val found in her brother's treasure box
    new_nickels = 2 * num_nickels

    # Calculate the total value of Val's new collection of coins in dollars
    total_value = 0.05 * (num_nickels + new_nickels) + 0.10 * num_dimes
    
    # Round the total value to 2 decimal places
    result = round(total_value, 2)
    return result

print(solution())