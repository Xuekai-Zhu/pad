def solution():
    """Jared wants to watch a series with four episodes. The first three episodes are 58 minutes, 62 minutes, and 65 minutes long respectively. If the four episodes last 4 hours, how long is the fourth episode?"""
    # Define the total duration of the first three episodes
    total_duration = 58 + 62 + 65

    # Calculate the remaining duration for the fourth episode
    remaining_duration = (4 * 60) - total_duration

    # Calculate the duration of the fourth episode
    fourth_duration = remaining_duration / 60

    # Display the duration of the fourth episode
    result = fourth_duration
    return result

print(solution())