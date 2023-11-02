def solution():
    ny_temp = 80  # Temperature in New York in June 2020 is 80 degrees
    miami_temp = ny_temp + 10  # Miami is 10 degrees hotter than New York
    san_diego_temp = miami_temp + 25  # San Diego is 25 degrees hotter than Miami

    # Calculate the average temperature for the three cities
    avg_temp = (ny_temp + miami_temp + san_diego_temp) / 3
    result = avg_temp
    return result

print(solution())