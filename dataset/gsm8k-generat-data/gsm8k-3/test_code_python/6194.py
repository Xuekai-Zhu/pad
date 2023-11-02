def solution():
    """Matt and Blake want to watch every episode of the show The Office. There are 201 episodes. If they watch 1 episode every Monday and 2 episodes every Wednesday each week, how many weeks will it take them to watch the whole series?"""
    # Define the number of episodes and episodes watched per week
    EPISODES = 201
    EPISODES_WATCHED_PER_WEEK = 3

    # Calculate the number of weeks needed to watch all episodes
    weeks = EPISODES // EPISODES_WATCHED_PER_WEEK
    if EPISODES % EPISODES_WATCHED_PER_WEEK != 0:
        weeks += 1

    # Display the number of weeks needed
    result = weeks
    return result

print(solution())