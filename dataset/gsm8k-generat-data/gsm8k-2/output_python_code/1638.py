def solution():
    """Ashley had already blown up 12 balloons for the party when Andy took over and started blowing them up at a rate of 2 every five minutes. When Andy stopped, there were 50 balloons. For how many minutes did Andy blow up balloons?"""
    initial_balloons = 12
    final_balloons = 50
    balloons_added = final_balloons - initial_balloons
    rate = 2 / 5  # balloons per minute
    time = balloons_added / rate
    result = time
    return result

print(solution())