def solution():
    """Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer’s market. The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil. One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour. If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour. What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?"""
    # Define the initial temperature of the warehouse
    initial_temp = 35

    # Calculate the temperature increase during the power outage
    temp_increase = 8 * 3

    # Calculate the temperature after the power outage
    post_outage_temp = initial_temp + temp_increase

    # Calculate the difference between the post-outage temperature and the target temperature
    temp_difference = post_outage_temp - 43

    # Calculate the number of hours needed for the air conditioner to restore the temperature to 43 degrees
    hours_needed = temp_difference / 4

    result = hours_needed
    return result

print(solution())