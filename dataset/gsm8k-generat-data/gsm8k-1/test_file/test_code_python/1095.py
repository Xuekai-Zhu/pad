def solution():
    """The biggest waterslide at Five Flags is 300 feet long, and people slide down at 60 feet/minute. The second biggest waterslide is 240 feet long, but steeper, so people slide down at 80 feet/minute. How much longer does it take to ride the biggest slide compared to the second biggest slide?"""
    length1 = 300
    speed1 = 60
    length2 = 240
    speed2 = 80
    time1 = length1 / speed1
    time2 = length2 / speed2
    difference = time1 - time2
    result = difference
    return result

print(solution())