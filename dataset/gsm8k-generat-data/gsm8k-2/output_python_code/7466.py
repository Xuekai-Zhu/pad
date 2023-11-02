def solution():
    """Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer’s market. The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil. One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour. If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour. What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?"""
    initial_temp = 35
    temp_rise = 8 * 3
    current_temp = initial_temp + temp_rise
    desired_temp = 43
    temp_drop_per_hour = 4
    time_to_desired_temp = (current_temp - desired_temp) / temp_drop_per_hour
    result = time_to_desired_temp
    return result

print(solution())