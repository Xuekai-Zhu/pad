def solution():
    
    # Define the rate of recharging per 3 minutes
    RATE_PER_3_MINUTES = 1 / 3

    # Define the percentage of charge that the phone is currently charged
    PERCENTAGE_CHARGE = 0.6

    # Calculate the time it will take to fully charge
    time_to_charge = 60 / (1 - PERCENTAGE_CHARGE) * 60

    # Convert the time to hours
    time_in_hours = time_to_charge / 60

    # Display the time it will take to fully charge in hours
    result = time_in_hours
    return result

print(solution())