def solution():
    distance = 12
    pace1 = 4
    pace2 = 6

    # Calculate the time it took to hike to Mount Overlook
    time1 = distance / pace1

    # Calculate the time it took to hike back from Mount Overlook
    time2 = distance / pace2

    # Calculate the total time of the hike
    total_time = time1 + time2
    result = total_time
    return result

print(solution())