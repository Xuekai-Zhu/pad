def solution():
    """Erin is watching a TV mini series of Pride and Prejudice. There are 6 episodes that are each 50 minutes long. If Erin watches all of the episodes in one sitting, one after the other with no breaks, how many hours will she spend watching the series?"""
    episodes = 6
    minutes_per_episode = 50
    total_minutes = episodes * minutes_per_episode
    hours = total_minutes / 60
    result = hours
    return result

print(solution())