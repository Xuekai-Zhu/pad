def solution():
    
    balloons = 52
    gallons_per_balloon = 5
    rate_1 = 8
    rate_2 = rate_1 / 2
    rate_3 = 2
    time_1 = 10
    time_2 = 5
    time_3 = (balloons * gallons_per_balloon - (rate_1 * time_1 + rate_2 * time_2)) / rate_3
    total_time = time_1 + time_2 + time_3
    result = total_time
    return result

print(solution())