def solution():
    nyc_temp = 80
    miami_temp = nyc_temp + 10
    sd_temp = miami_temp + 25

    # Calculate the average temperature for the three cities
    avg_temp = (nyc_temp + miami_temp + sd_temp) / 3
    result = avg_temp
    return result

print(solution())