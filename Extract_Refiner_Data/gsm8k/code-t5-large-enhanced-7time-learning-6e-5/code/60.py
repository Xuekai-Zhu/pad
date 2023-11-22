def solution():
    
    # Define the distance traveled and the amount of gas needed to fill up the tank
    distance_traveled = 100
    gas_needed = 4

    # Define the size of the gas tank in gallons
    gas_tank_size = 12

    # Calculate the total amount of gas used in the trip
    gas_used = gas_needed / gas_tank_size

    # Calculate the distance Sophia can drive on a single tank of gas
    gas_drive = distance_traveled + gas_used

    # Display the distance Sophia can drive on a single tank of gas
    result = gas_drive
    return result

print(solution())