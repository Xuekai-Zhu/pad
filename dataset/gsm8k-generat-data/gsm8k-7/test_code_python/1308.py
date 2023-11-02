def solution():
    total_time = 0
    total_time += 12  # half the day on Monday
    total_time += 4   # 4 hours on Tuesday
    total_time += 6   # quarter of the day on Wednesday (6 hours)
    total_time *= 1.5 # half as much time on Thursday
    completed_time = 52 # total time for the show

    # Calculate the time Jake watched on Friday
    friday_time = completed_time - total_time
    result = friday_time
    return result

print(solution())