def solution():
    # Calculate the time for the first leg of the journey
    time1 = 0.5 # 30 minutes in hours
    distance1 = 10 * time1

    # Calculate the time for the second leg of the journey
    distance2 = 15
    speed2 = (distance2 / time1) / 60
    time2 = distance2 / speed2

    # Add the rest time
    rest_time = 0.5

    # Calculate the time for the final leg of the journey
    distance3 = 20
    speed3 = 10
    time3 = distance3 / speed3

    # Calculate the total time
    total_time = time1 + time2 + rest_time + time3
    result = total_time * 60
    return result

print(solution())