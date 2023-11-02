def solution():
    """Max watches a show every day that airs from 2:00 pm to 2:30 pm and only airs during weekdays. If he watches every episode during the week but misses the Friday episode, how many hours of the show did he watch?"""
    # Define the length of each episode in hours
    EPISODE_LENGTH = 0.5

    # Define the number of episodes watched from Monday to Thursday
    episodes_watched = 4

    # Calculate the total length of episodes watched
    total_length = episodes_watched * EPISODE_LENGTH

    # Display the total length of episodes watched
    result = total_length
    return result

print(solution())