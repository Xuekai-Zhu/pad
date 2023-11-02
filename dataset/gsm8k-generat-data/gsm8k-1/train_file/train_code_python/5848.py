def solution():
    """Max watches a show every day that airs from 2:00 pm to 2:30 pm and only airs during weekdays. If he watches every episode during the week but misses the Friday episode, how many hours of the show did he watch?"""
    start_time = 2.0
    end_time = 2.5
    days_watched = 4
    episode_length = end_time - start_time
    total_time = episode_length * days_watched
    result = total_time
    return result

print(solution())