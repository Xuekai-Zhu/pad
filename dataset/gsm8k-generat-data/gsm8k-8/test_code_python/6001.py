def solution():
    # Define the daily temperatures
    sunday_temp = 99.1
    monday_temp = 98.2
    tuesday_temp = 98.7
    wednesday_temp = 99.3
    thursday_temp = 99.8
    friday_temp = 99.0
    saturday_temp = 98.9

    # Calculate the average temperature
    average_temp = (sunday_temp + monday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp) / 7
    result = average_temp
    return result

print(solution())