def solution():
    # Define the number of balloons that Ashley blew up
    ashley_balloons = 12

    # Define the number of balloons that Andy added
    andy_balloons = 50 - ashley_balloons

    # Convert the rate of balloons blown up to balloons per minute
    balloons_per_minute = 2 / 5

    # Calculate the number of minutes it took Andy to blow up the remaining balloons
    andy_minutes = andy_balloons / balloons_per_minute

    result = andy_minutes
    return result

print(solution())