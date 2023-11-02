def solution():
    """Melinda is taking a 1200-mile trip with her family to visit their cousins. How much time will they save if they drive 60 miles an hour instead of 50 miles an hour?"""
    distance = 1200
    speed1 = 50
    speed2 = 60
    time1 = distance / speed1
    time2 = distance / speed2
    time_saved = time1 - time2
    result = time_saved
    return result

print(solution())