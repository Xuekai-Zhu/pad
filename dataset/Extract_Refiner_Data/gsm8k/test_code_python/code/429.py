def solution():
    
    # Define the total amount of gas in gallons
    total_gallons = 15

    # Calculate the amount of gas in each container
    gas_per_container = total_gallons / 5

    # Calculate the amount of gas needed for the lawnmower
    gas_needed = gas_per_container / 4

    # Convert the amount of gas needed to pints
    gas_needed_pints = gas_needed * 8

    # Display the amount of gas needed in pints
    result = gas_needed_pints
    return result

print(solution())