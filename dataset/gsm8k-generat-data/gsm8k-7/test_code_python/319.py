def solution():
    initial_diaries = 8
    bought_diaries = initial_diaries * 2
    lost_diaries = bought_diaries / 4
    final_diaries = bought_diaries - lost_diaries
    result = final_diaries
    return result

print(solution())