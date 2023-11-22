def solution():
    
    # Define the value of each coin return in cents
    quarter_value = 0.25
    nickel_value = 0.05
    dime_value = 0.10

    # Calculate the total value of the vending machine in cents
    total_value = (quarter_value * 25) + (nickel_value * 5) + (dime_value * 10)

    # Display the total value in cents
    result = total_value
    return result

print(solution())