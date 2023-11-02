def solution():
    # Calculate the total minutes of the TV show watched by Maddie
    total_minutes = 8 * 44  # 8 episodes, each episode is about 44 minutes long
    total_minutes -= 138 + 0 + 0 + 21  # subtract the minutes watched on Monday, Tuesday, Wednesday, and Thursday
    total_minutes += 2 * 44  # add the minutes watched on Friday, which is 2 episodes
    result = total_minutes
    return result

print(solution())