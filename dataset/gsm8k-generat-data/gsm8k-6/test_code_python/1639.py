def solution():
    # Calculate the number of balloons Andy blew up
    balloons_blowed = 50 - 12  # Andy stopped when there were 50 balloons, and Ashley had already blown up 12 balloons
    # Calculate the time Andy spent blowing up the balloons in minutes
    time_blowing_balloons = (balloons_blowed/2) * 5  # Andy was blowing up 2 balloons every 5 minutes
    result = time_blowing_balloons
    return result

print(solution())