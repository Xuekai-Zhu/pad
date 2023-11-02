def solution():
    rain_in_march = 3.79
    rain_in_april = 4.5
    rain_in_may = 3.95
    rain_in_june = 3.09
    rain_in_july = 4.67

    # Calculate the total rainfall over the five months
    total_rainfall = rain_in_march + rain_in_april + rain_in_may + rain_in_june + rain_in_july

    # Calculate the average rainfall
    average_rainfall = total_rainfall / 5
    result = average_rainfall
    return result

print(solution())