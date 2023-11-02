def solution():
    """Maddie watches 8 episodes of a TV show this week. Each episode is about 44 minutes long. If she watches 138 minutes of the show on Monday. She does not watch any TV on Tuesday and Wednesday. On Thursday, she watches 21 minutes. On Friday, she watches 2 episodes. How many more minutes did she watch over the weekend?"""
    # Define the length of each episode
    EPISODE_LENGTH = 44

    # Calculate the total length of the show Maddie watched
    total_length = 8 * EPISODE_LENGTH

    # Subtract the length of the show Maddie watched on Monday, Thursday, and Friday
    total_length -= 138 + 21 + 2 * EPISODE_LENGTH

    # The remaining length is what Maddie watched over the weekend
    weekend_length = total_length

    # Display the length of the show Maddie watched over the weekend
    result = weekend_length
    return result

print(solution())