def solution():
    # Calculate the number of episodes watched from Monday to Thursday
    episodes_watched = 4  # Max watches every episode during the week
    time_per_episode = 0.5  # Each episode is 30 minutes long
    total_time_watched = episodes_watched * time_per_episode

    # Return the total number of hours of the show Max watched
    result = total_time_watched / 2  # The show airs for half an hour each day
    return result

print(solution())