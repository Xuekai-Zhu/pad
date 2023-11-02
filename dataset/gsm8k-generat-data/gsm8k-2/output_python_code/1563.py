def solution():
    """Maddie watches 8 episodes of a TV show this week. Each episode is about 44 minutes long. If she watches 138 minutes of the show on Monday. She does not watch any TV on Tuesday and Wednesday. On Thursday, she watches 21 minutes. On Friday, she watches 2 episodes. How many more minutes did she watch over the weekend?"""
    episodes_this_week = 8
    mins_per_episode = 44
    mon_mins = 138
    thu_mins = 21
    fri_eps = 2
    fri_mins = fri_eps * mins_per_episode
    weekend_mins = (episodes_this_week * mins_per_episode) - mon_mins - thu_mins - fri_mins
    result = weekend_mins
    return result

print(solution())