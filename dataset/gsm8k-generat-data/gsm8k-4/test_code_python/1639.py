def solution():
    """Ashley had already blown up 12 balloons for the party when Andy took over and started blowing them up at a rate of 2 every five minutes. When Andy stopped, there were 50 balloons. For how many minutes did Andy blow up balloons?"""
    # Define the number of balloons Ashley had blown up
    ashley_balloons = 12

    # Define the total number of balloons
    total_balloons = 50

    # Define the rate at which Andy was blowing up balloons
    andy_rate = 2/5 # 2 balloons every 5 minutes

    # Calculate the number of balloons Andy blew up
    andy_balloons = total_balloons - ashley_balloons

    # Calculate the time it took for Andy to blow up the balloons
    andy_time = andy_balloons / andy_rate

    # return the result in minutes
    result = andy_time * 60
    return result

print(solution())