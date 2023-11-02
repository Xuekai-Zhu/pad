def solution():
    """Melinda is taking a 1200-mile trip with her family to visit their cousins. How much time will they save if they drive 60 miles an hour instead of 50 miles an hour?"""
    distance = 1200
    speed_1 = 50
    speed_2 = 60
    time_1 = distance / speed_1
    time_2 = distance / speed_2
    time_saved = time_1 - time_2
    result = time_saved
    return result

print(solution())