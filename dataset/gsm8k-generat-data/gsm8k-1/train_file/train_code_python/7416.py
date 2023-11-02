def solution():
    """Max fills up water balloons for 30 minutes at a rate of 2 water balloons every minute. Max’s friend Zach fills up water balloons for 40 minutes at a rate of 3 water balloons every minute. In the process, 10 of the water balloons pop on the ground. How many filled water balloons do Max and Zach have in total?"""
    max_time = 30
    max_rate = 2
    zach_time = 40
    zach_rate = 3
    max_filled = max_time * max_rate
    zach_filled = zach_time * zach_rate
    total_filled = max_filled + zach_filled - 10
    result = total_filled
    return result

print(solution())