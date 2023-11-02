def solution():
    """It is raining outside and Bill puts his empty fish tank in his yard to let it fill with rainwater. It starts raining at 1 pm. 2 inches of rainfall in the first hour. For the next four hours, it rains at a rate of 1 inch per hour. It then rains at three inches per hour for the rest of the day. If the fish tank is 18 inches tall, at what time will it be filled with rainwater."""
    # Define the height of the fish tank
    fish_tank_height = 18

    # Define the initial amount of rainfall in inches and the time it started raining
    initial_rainfall = 2
    start_time = 1

    # Define the amount of rainfall for the next four hours
    four_hour_rainfall = 4

    # Define the rate of rainfall for the remaining hours
    hourly_rainfall = 3

    # Calculate the total rainfall needed to fill the fish tank
    total_rainfall = fish_tank_height - initial_rainfall - four_hour_rainfall
    time = start_time + 5 + total_rainfall / hourly_rainfall

    # Return the time in 24-hour format
    result = str(int(time)) + ":00"
    return result

print(solution())