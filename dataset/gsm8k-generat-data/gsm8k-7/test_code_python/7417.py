def solution():
    max_time = 30            # in minutes
    max_rate = 2             # in water balloons/min
    max_total = max_time * max_rate     # total water balloons filled by Max

    zach_time = 40           # in minutes
    zach_rate = 3            # in water balloons/min
    zach_total = zach_time * zach_rate   # total water balloons filled by Zach

    total_balloons = max_total + zach_total - 10   # total water balloons after subtracting the popped ones

    result = total_balloons
    return result

print(solution())