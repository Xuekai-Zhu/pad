def solution():
    """John buys 20 hours of music a month. The average length of a song is 3 minutes. He buys each song for $.50. How much does he pay for music a year?"""
    # Define the number of songs he buys each month
    minutes_in_hour = 60
    songs_in_hour = 60 / 3
    songs_per_month = songs_in_hour * 20

    # Define the cost per song and calculate the total cost per month
    cost_per_song = 0.5
    total_cost_per_month = songs_per_month * cost_per_song

    # Calculate the total cost per year
    total_cost_per_year = total_cost_per_month * 12

    # return the result
    result = total_cost_per_year
    return result

print(solution())