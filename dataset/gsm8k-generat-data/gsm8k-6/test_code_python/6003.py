def solution():
    # Calculate the time taken for the first part of the journey
    time_first = 30 / 60  # 30 minutes to hours

    # Calculate the time taken for the second part of the journey
    time_second = (15 / 10) + (30 / 60)  # time = distance / speed + resting time

    # Calculate the time taken for the third part of the journey
    time_third = 20 / 10

    # Calculate the total time taken
    total_time = (time_first + time_second + time_third) * 60  # convert total time to minutes
    result = total_time
    return result

print(solution())