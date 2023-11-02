def solution():
    weekly_goal = 3500
    track_length = 50
    num_loops_per_day = weekly_goal / 7 / track_length
    result = num_loops_per_day
    return result

print(solution())