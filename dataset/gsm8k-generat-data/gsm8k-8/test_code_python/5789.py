def solution():
    # Calculate the time spent walking on Monday (distance / rate)
    monday_time = 6 / 2

    # Calculate the time spent walking on Wednesday
    wednesday_time = 6 / 3

    # Calculate the time spent running on Friday
    friday_time = 6 / 6

    # Calculate the combined total time spent exercising in a week
    total_time = monday_time + wednesday_time + friday_time

    result = total_time
    return result

print(solution())