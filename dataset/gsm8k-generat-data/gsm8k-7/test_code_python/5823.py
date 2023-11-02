def solution():
    drips_per_minute = 10
    drops_per_drip = 1
    volume_per_drop = 0.05
    minutes_per_hour = 60

    # Calculate the total number of drops per hour
    drops_per_hour = drips_per_minute * drops_per_drip * minutes_per_hour

    # Calculate the total volume of water wasted per hour
    volume_wasted_per_hour = drops_per_hour * volume_per_drop

    result = volume_wasted_per_hour
    return result

print(solution())