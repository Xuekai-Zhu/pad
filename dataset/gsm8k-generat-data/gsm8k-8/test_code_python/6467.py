def solution():
    # Define the temperature in New York
    ny_temp = 80

    # Calculate the temperature in Miami and San Diego
    miami_temp = ny_temp + 10
    sd_temp = miami_temp + 25

    # Calculate the average temperature for the three cities
    avg_temp = (ny_temp + miami_temp + sd_temp) / 3
    result = avg_temp
    return result

print(solution())