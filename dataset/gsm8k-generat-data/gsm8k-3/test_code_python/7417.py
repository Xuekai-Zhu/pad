def solution():
    """Max fills up water balloons for 30 minutes at a rate of 2 water balloons every minute. Max’s friend Zach fills up water balloons for 40 minutes at a rate of 3 water balloons every minute. In the process, 10 of the water balloons pop on the ground. How many filled water balloons do Max and Zach have in total?"""
    # Calculate the number of water balloons Max fills up
    max_rate = 2 # balloons/minute
    max_time = 30 # minutes
    max_balloons = max_rate * max_time

    # Calculate the number of water balloons Zach fills up
    zach_rate = 3 # balloons/minute
    zach_time = 40 # minutes
    zach_balloons = zach_rate * zach_time

    # Calculate the total number of filled water balloons
    total_balloons = max_balloons + zach_balloons - 10

    result = total_balloons
    return result

print(solution())