def solution():
    sitting_time = 360  # 6 hours = 360 minutes
    walking_time = sitting_time // 90 * 10  # floor division to get number of 90-minute blocks, then multiply by 10

    result = walking_time
    return result

print(solution())