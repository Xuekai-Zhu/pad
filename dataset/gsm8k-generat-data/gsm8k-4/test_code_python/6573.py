def solution():
    """Andy is making fudge. First he needs to raise the temperature of the candy mixture from 60 degrees to 240 degrees. Then he needs to cool it down to 170 degrees. If the candy heats at 5 degrees/minute and cools at 7 degrees/minute, how long will it take for the candy to be done (in minutes)?"""
    # Define the starting and target temperatures
    starting_temp = 60
    target_temp = 240
    cool_temp = 170

    # Calculate the time to heat the mixture
    heat_time = (target_temp - starting_temp) / 5

    # Calculate the time to cool the mixture
    cool_time = (target_temp - cool_temp) / 7

    # Calculate the total time for the candy to be done
    total_time = heat_time + cool_time

    # return the result
    result = total_time
    return result

print(solution())