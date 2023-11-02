def solution():
    """Max watches a show every day that airs from 2:00 pm to 2:30 pm and only airs during weekdays. If he watches every episode during the week but misses the Friday episode, how many hours of the show did he watch?"""
    # Calculate the duration of each episode in hours
    episode_duration = 0.5 / 60

    # Calculate the number of weekdays in a week
    weekdays_per_week = 5

    # Calculate the total duration of watched episodes
    total_duration = weekdays_per_week * episode_duration

    # Return the result
    result = total_duration * 60
    return result

print(solution())