def solution():
    total_episodes = 201
    episodes_per_week = 1 + 2 # 1 on Monday, 2 on Wednesday
    num_weeks = total_episodes / episodes_per_week
    result = num_weeks
    return result

print(solution())