def solution():
    
    desired_hourly_pay = 10
    cents_per_weed = 5
    weeds_per_hour = (desired_hourly_pay * 100) / cents_per_weed
    seconds_per_weed = 60 * 60 / weeds_per_hour
    result = seconds_per_weed
    return result

print(solution())