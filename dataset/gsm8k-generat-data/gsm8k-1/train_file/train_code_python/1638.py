def solution():
    """Ashley had already blown up 12 balloons for the party when Andy took over and started blowing them up at a rate of 2 every five minutes. When Andy stopped, there were 50 balloons. For how many minutes did Andy blow up balloons?"""
    # First we need to find out how many balloons Andy blew up
    balloons_before = 12
    balloons_after = 50
    balloons_blow_up_by_andy = balloons_after - balloons_before
    
    # Next we need to find out how many times Andy blew up balloons (each time blowing up 2 balloons)
    balloons_per_blow_up = 2
    total_blow_ups = balloons_blow_up_by_andy / balloons_per_blow_up
    
    # Finally we need to find out how many total minutes Andy spent blowing up balloons
    minutes_per_blow_up = 5
    total_minutes = total_blow_ups * minutes_per_blow_up
    
    result = total_minutes
    return result

print(solution())