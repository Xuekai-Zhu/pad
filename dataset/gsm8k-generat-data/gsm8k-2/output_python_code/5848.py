def solution():
    """Max watches a show every day that airs from 2:00 pm to 2:30 pm and only airs during weekdays. If he watches every episode during the week but misses the Friday episode, how many hours of the show did he watch?"""
    # The show is 30 minutes long
    show_duration = 0.5
    # There are 5 weekdays in a week
    weekdays = 5
    # Max watches every weekday except Friday
    watched_episodes = weekdays - 1
    # Calculate the total time Max spent watching the show
    total_time = show_duration * watched_episodes
    result = total_time
    return result

print(solution())