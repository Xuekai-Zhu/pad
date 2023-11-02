def solution():
    # Define the values of a loonie and a toonie
    loonie_value = 1
    toonie_value = 2
    
    # Define the total value of the coins in Antonella's purse
    total_value = 10 * loonie_value
    
    # Calculate the number of toonies Antonella initially had
    initial_toonies = (total_value - 3 - 11) / (toonie_value - loonie_value)
    
    result = initial_toonies
    return result

print(solution())