def solution():
    total_episodes = 201  # There are 201 episodes in The Office
    episodes_per_week = 1 + 2 + 1  # They watch 1 episode on Monday and 2 on Wednesday and take one day off
    weeks = total_episodes / episodes_per_week  # Calculate the total number of weeks required to watch all episodes

    # Round up the number of weeks to the nearest integer
    weeks = math.ceil(weeks)
    result = weeks
    return result

print(solution())