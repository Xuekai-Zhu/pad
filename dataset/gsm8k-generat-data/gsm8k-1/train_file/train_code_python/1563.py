def solution():
    """Maddie watches 8 episodes of a TV show this week. Each episode is about 44 minutes long. If she watches 138 minutes of the show on Monday. She does not watch any TV on Tuesday and Wednesday. On Thursday, she watches 21 minutes. On Friday, she watches 2 episodes. How many more minutes did she watch over the weekend?"""
    total_episodes = 8
    minutes_per_episode = 44
    monday_minutes = 138
    thursday_minutes = 21
    friday_episodes = 2
    friday_minutes = friday_episodes * minutes_per_episode
    weekend_minutes = (total_episodes * minutes_per_episode) - (monday_minutes + thursday_minutes + friday_minutes)
    result = weekend_minutes
    return result

print(solution())