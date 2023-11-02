def solution():
    total_episodes = 90  # The show has 90 episodes
    episode_length = 20  # Each episode is 20 minutes long
    daily_time = 120  # Tom can spend 2 hours (120 minutes) a day watching the show

    # Calculate the total time required to finish watching the show
    total_time = total_episodes * episode_length

    # Calculate the number of days Tom will take to finish watching the show
    days_to_finish = total_time / daily_time
    result = days_to_finish
    return result

print(solution())