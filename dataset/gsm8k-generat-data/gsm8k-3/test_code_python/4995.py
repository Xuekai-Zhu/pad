def solution():
    """John buys 20 hours of music a month. The average length of a song is 3 minutes. He buys each song for $.50. How much does he pay for music a year?"""
    # Define the length of each song in minutes
    SONG_LENGTH = 3

    # Calculate the number of songs John buys in a month
    songs_per_month = (20 * 60) // SONG_LENGTH

    # Calculate the cost of the songs John buys in a month
    cost_per_month = songs_per_month * 0.5

    # Calculate the cost of the songs John buys in a year
    cost_per_year = cost_per_month * 12

    # Display the cost of the songs John buys in a year
    result = cost_per_year
    return result

print(solution())