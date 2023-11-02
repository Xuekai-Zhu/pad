def solution():
    # Calculate the time it takes to raise the temperature to 240 degrees
    temp_change = 240 - 60  # temperature needs to increase by 180 degrees
    time_to_heat = temp_change / 5  # the candy heats at 5 degrees/minute

    # Calculate the time it takes to cool the candy down to 170 degrees
    temp_change = 240 - 170  # temperature needs to decrease by 70 degrees
    time_to_cool = temp_change / 7  # the candy cools at 7 degrees/minute

    # Calculate the total time it takes to make the fudge
    total_time = time_to_heat + time_to_cool
    result = total_time
    return result

print(solution())