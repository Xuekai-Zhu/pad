def solution():
    # Calculate current number of diaries
    orig_diaries = 8  # original number of diaries
    bought_diaries = 2 * orig_diaries  # double the original number of diaries
    lost_diaries = bought_diaries / 4  # 1/4 of the bought diaries were lost
    current_diaries = bought_diaries - lost_diaries  # calculate current number of diaries
    result = current_diaries
    return result

print(solution())