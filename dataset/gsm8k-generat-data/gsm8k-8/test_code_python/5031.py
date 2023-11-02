def solution():
    # Calculate the total time Gretchen spends sitting
    sitting_time = 6 * 60  # 6 hours in minutes

    # Calculate the number of 90-minute periods Gretchen spends sitting
    sitting_periods = sitting_time // 90

    # Calculate the total walking time based on the sitting periods
    walking_time = sitting_periods * 10

    result = walking_time
    return result

print(solution())