def solution():
    """A hot air balloon with 200 balloons is blowing up. After about half an hour, 1/5 of the total number of balloons in the hot air balloon have blown up. After another hour, twice the number of balloons that had already blown up also blow up. How many balloons in the hot air balloon remain intact?"""
    # Define the initial number of balloons
    balloons = 200

    # Calculate the number of balloons blown up after half an hour
    balloons_blown_half_hour = balloons * (1/5)

    # Calculate the number of balloons remaining after half an hour
    balloons_remaining_half_hour = balloons - balloons_blown_half_hour

    # Calculate the number of balloons blown up after another hour
    balloons_blown_another_hour = balloons_blown_half_hour * 2

    # Calculate the number of balloons remaining after another hour
    balloons_remaining_another_hour = balloons_remaining_half_hour - balloons_blown_another_hour

    # Return the final number of intact balloons
    result = balloons_remaining_another_hour
    return result

print(solution())