def solution():
    """Prejean's speed in a race was three-quarters that of Rickey. If they both took a total of 70 minutes to run the race, calculate the total number of minutes that Rickey took to finish the race."""
    total_time = 70
    prejean_speed_ratio = 0.75
    rickey_speed_ratio = 1 - prejean_speed_ratio
    rickey_time = (total_time * rickey_speed_ratio) / (prejean_speed_ratio + rickey_speed_ratio)
    result = rickey_time
    return result

print(solution())