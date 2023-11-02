def solution():
    """It is raining outside and Bill puts his empty fish tank in his yard to let it fill with rainwater. It starts raining at 1 pm. 2 inches of rainfall in the first hour. For the next four hours, it rains at a rate of 1 inch per hour. It then rains at three inches per hour for the rest of the day. If the fish tank is 18 inches tall, at what time will it be filled with rainwater."""
    tank_height = 18
    total_rainfall = 2 + (4 * 1) + ((24 - 5) * 3)  # calculate total rainfall in inches
    time_to_fill = tank_height / total_rainfall * 60  # convert time to minutes
    result = "The fish tank will be filled with rainwater at {} pm.".format(
        int(time_to_fill/60) + 1)  # add 1 to account for starting at 1 pm

    return result

print(solution())