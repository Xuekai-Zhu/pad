def solution():
    """It is raining outside and Bill puts his empty fish tank in his yard to let it fill with rainwater. It starts raining at 1 pm. 2 inches of rainfall in the first hour. For the next four hours, it rains at a rate of 1 inch per hour. It then rains at three inches per hour for the rest of the day. If the fish tank is 18 inches tall, at what time will it be filled with rainwater."""
    # Define the height of the fish tank and the rainfall rates
    TANK_HEIGHT = 18
    RAINFALL_RATES = [2, 1, 1, 1, 1, 3]

    # Calculate the total rainfall over the day
    total_rainfall = sum(RAINFALL_RATES)

    # Calculate the time it takes to fill the fish tank
    tank_fill_time = TANK_HEIGHT / total_rainfall

    # Convert the time to hours and minutes
    hours = int(tank_fill_time)
    minutes = int((tank_fill_time - hours) * 60)

    # Display the time it takes to fill the fish tank
    result = f"{hours}:{minutes:02}"
    return result

print(solution())