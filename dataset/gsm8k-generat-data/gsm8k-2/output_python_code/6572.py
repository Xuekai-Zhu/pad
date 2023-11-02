def solution():
    """Andy is making fudge. First he needs to raise the temperature of the candy mixture from 60 degrees to 240 degrees. Then he needs to cool it down to 170 degrees. If the candy heats at 5 degrees/minute and cools at 7 degrees/minute, how long will it take for the candy to be done (in minutes)?"""
    initial_temp = 60
    heat_rate = 5
    target_temp_1 = 240
    cool_rate = 7
    target_temp_2 = 170

    # calculate time to heat up
    time_to_heat = (target_temp_1 - initial_temp) / heat_rate

    # calculate time to cool down
    time_to_cool = (target_temp_1 - target_temp_2) / cool_rate

    # total time
    total_time = time_to_heat + time_to_cool

    result = total_time
    return result

print(solution())