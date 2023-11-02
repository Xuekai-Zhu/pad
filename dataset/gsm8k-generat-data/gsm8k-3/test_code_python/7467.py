def solution():
    """Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer’s market.  The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil.  One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour.  If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour.  What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?"""
    # Initialize the temperature and time variables
    temperature = 51 # temperature after 3 hours
    time = 0

    # Calculate the time it will take for the air conditioner to restore the temperature to 43 degrees F
    while temperature > 43:
        temperature -= 4 # temperature decreases by 4 degrees per hour
        time += 1

    # Display the time it will take for the air conditioner to restore the temperature
    result = time
    return result

print(solution())