def solution():
    episodes_watched = 8  # Maddie watched 8 episodes in total
    episode_length = 44  # Each episode is 44 minutes long

    # Calculate the total length of the episodes Maddie watched
    total_length = episodes_watched * episode_length

    # Subtract the minutes watched on Monday, Thursday, and Friday to get the minutes watched on the weekend
    weekend_minutes = total_length - 138 - 21 - (2 * episode_length)

    result = weekend_minutes
    return result

print(solution())