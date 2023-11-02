def solution():
    # Calculate the total time Max spent on his homework
    biology_time = 20  # minutes
    history_time = 2 * biology_time  # twice the time he spent on biology
    geography_time = 3 * history_time  # three times the time he spent on history
    total_time = biology_time + history_time + geography_time
    result = total_time
    return result

print(solution())