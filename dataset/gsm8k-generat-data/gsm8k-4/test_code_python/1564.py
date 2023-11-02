def solution():
    """Maddie watches 8 episodes of a TV show this week. Each episode is about 44 minutes long. If she watches 138 minutes of the show on Monday. She does not watch any TV on Tuesday and Wednesday. On Thursday, she watches 21 minutes. On Friday, she watches 2 episodes. How many more minutes did she watch over the weekend?"""
    # Define the number of episodes and the length of each episode
    episodes = 8
    episode_length = 44

    # Calculate the total time Maddie spent watching the show from Monday to Thursday
    total_time = 138 + 0 + 0 + 21

    # Calculate the total time Maddie spent watching the show on Friday
    friday_time = 2 * episode_length

    # Calculate the total time Maddie spent watching the show from Saturday to Sunday
    weekend_time = (episodes - 2) * episode_length - friday_time

    # Calculate the total time Maddie spent watching the show during the week
    total_time += friday_time + weekend_time

    # Return the number of minutes Maddie watched over the weekend
    result = weekend_time
    return result

print(solution())