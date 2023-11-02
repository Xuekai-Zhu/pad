def solution():
    initial_diaries = 8  # Natalie's sister had 8 small diaries in her locker
    bought_diaries = initial_diaries * 2  # She bought double the number of diaries she had
    lost_diaries = bought_diaries / 4  # She lost 1/4 of the diaries she bought
    total_diaries = bought_diaries - lost_diaries  # Total number of diaries she has now

    result = total_diaries
    return result

print(solution())