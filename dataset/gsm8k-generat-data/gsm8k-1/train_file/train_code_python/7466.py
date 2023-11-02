def solution():
    """Roy owns a refrigerated warehouse where he stores produce before selling it at the farmer’s market. The fruits and vegetables he stores are very sensitive to temperature, and he must keep them all cold or they will spoil. One day, the power went out and the air conditioner was turned off for three hours, during which time the temperature rose by 8 degrees per hour. If Roy gets the power back on, it will activate the air conditioner to lower the temperature at the rate of 4 degrees F per hour. What is the amount of time, in hours, it will take for the air conditioner to restore the warehouse to 43 degrees F?"""
    initial_temp = 43
    temp_rise_per_hour = 8
    temp_fall_per_hour = 4
    time_elapsed = 3
    temp_rise = temp_rise_per_hour * time_elapsed
    net_temp_change = initial_temp + temp_rise
    time_needed = (net_temp_change - initial_temp) / temp_fall_per_hour
    result = time_needed
    return result

print(solution())