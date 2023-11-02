def solution():
    """Tom is binge-watching a show on Netflix. The show has 90 episodes, each one of which is 20 minutes long because there are no commercials. If Tom can spend two hours a day watching the show, how many days will it take him to finish watching the show?"""
    # Define the length of each episode in minutes
    EPISODE_LENGTH = 20

    # Define the total number of episodes
    total_episodes = 90

    # Calculate the total length of the show in minutes
    show_length = total_episodes * EPISODE_LENGTH

    # Calculate the number of minutes Tom can spend watching the show each day
    daily_allowed_minutes = 2 * 60

    # Calculate the number of days it will take Tom to finish the show
    days_to_finish = show_length / daily_allowed_minutes

    # Return the number of days rounded up to the nearest integer
    result = math.ceil(days_to_finish)
    return result

print(solution())