def solution():
    half_hour_show_length = 0.5  # Half-hour show has a length of 0.5 hours
    hour_long_show_length = 1  # 1-hour show has a length of 1 hour
    half_hour_show_episodes = 24  # Tim watches 24 episodes of the half-hour show
    hour_long_show_episodes = 12  # Tim watches 12 episodes of the 1-hour show

    # Calculate the total hours Tim spent watching the half-hour show
    half_hour_show_hours = half_hour_show_length * half_hour_show_episodes

    # Calculate the total hours Tim spent watching the 1-hour show
    hour_long_show_hours = hour_long_show_length * hour_long_show_episodes

    # Calculate the total hours Tim spent watching TV
    total_hours = half_hour_show_hours + hour_long_show_hours
    result = total_hours
    return result

print(solution())