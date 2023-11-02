def solution():
    # Calculate the total time Gretchen spends sitting
    sitting_time = 6 * 60  # 6 hours in minutes

    # Calculate the total time Gretchen should spend walking
    walking_time = (sitting_time // 90) * 10  # every 90 minutes sitting requires 10 minutes of walking

    result = walking_time
    return result

print(solution())