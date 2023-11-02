def solution():
    """When Harriett vacuumed the sofa and chair she found 10 quarters, 3 dimes, 3 nickels, and 5 pennies.  How much money did Harriett find?"""
    
    # Define the value of each coin
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01
    
    # Calculate the total value of the found coins
    total_value = 10 * quarter_value + 3 * dime_value + 3 * nickel_value + 5 * penny_value
    
    # Round the total value to 2 decimal places
    total_value = round(total_value, 2)
    
    # Display the total value
    result = total_value
    return result

print(solution())