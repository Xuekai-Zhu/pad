def solution():
    """Ashley had already blown up 12 balloons for the party when Andy took over and started blowing them up at a rate of 2 every five minutes. When Andy stopped, there were 50 balloons. For how many minutes did Andy blow up balloons?"""
    # Determine the number of balloons Andy blew up
    balloons_blow_up = 50 - 12

    # Determine the time it took for Andy to blow up the balloons
    time_in_minutes = (balloons_blow_up / 2) * 5

    # Display the time Andy spent blowing up balloons
    result = time_in_minutes
    return result

print(solution())