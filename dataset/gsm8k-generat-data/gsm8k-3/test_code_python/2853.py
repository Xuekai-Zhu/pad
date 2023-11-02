def solution():
    """Tim host a show and they film multiple episodes per day.  Each episode is 20 minutes long and it takes 50% longer than that to film each episode.  Each week they show 5 episodes.  How many hours would it take to film 4 weeks of episodes?"""
    # Define the length of each episode and the filming time
    EPISODE_LENGTH = 20
    FILMING_TIME_MULTIPLIER = 1.5

    # Define the number of episodes per week and per 4 weeks
    EPISODES_PER_WEEK = 5
    EPISODES_PER_4_WEEKS = 20

    # Calculate the filming time for each episode and the total filming time for each week and 4 weeks
    filming_time_per_episode = EPISODE_LENGTH * FILMING_TIME_MULTIPLIER
    filming_time_per_week = filming_time_per_episode * EPISODES_PER_WEEK
    filming_time_per_4_weeks = filming_time_per_week * 4 / 60

    # Display the total filming time for 4 weeks in hours
    result = filming_time_per_4_weeks
    return result

print(solution())