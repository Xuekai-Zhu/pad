def solution():
    num_episodes = 227
    min_per_episode = 45 #average of 42-47
    total_series_length = num_episodes * min_per_episode
    minutes_in_six_months = 6 * 30 * 24 * 60 #assuming 30 days per month
    if total_series_length <= minutes_in_six_months:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())