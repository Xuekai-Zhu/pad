def solution():
    """Andy is making fudge. First he needs to raise the temperature of the candy mixture from 60 degrees to 240 degrees. Then he needs to cool it down to 170 degrees. If the candy heats at 5 degrees/minute and cools at 7 degrees/minute, how long will it take for the candy to be done (in minutes)?"""
    # Calculate the amount of time it takes to heat the candy mixture to 240 degrees
    heat_time = (240 - 60) / 5

    # Calculate the amount of time it takes to cool the candy mixture to 170 degrees
    cool_time = (240 - 170) / 7

    # Calculate the total amount of time it takes for the candy mixture to be done
    total_time = heat_time + cool_time

    # Display the total amount of time
    result = total_time
    return result

print(solution())