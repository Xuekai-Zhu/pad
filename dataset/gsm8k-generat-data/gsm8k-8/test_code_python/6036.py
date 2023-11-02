def solution():
    # Calculate the total amount of rain that falls during the day
    total_rain = 2 + 4*1 + 3*7

    # Calculate the time it takes to fill the fish tank
    time_to_fill = 18 / total_rain

    # Calculate the time it will be filled after it starts raining
    fill_time = 1 + time_to_fill

    result = fill_time
    return result

print(solution())