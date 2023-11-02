def solution():
    music_hours_per_month = 20  # John buys 20 hours of music per month
    music_minutes_per_hour = 60  # There are 60 minutes in an hour
    song_length_in_minutes = 3  # The average length of a song is 3 minutes
    cost_per_song = 0.5  # John pays $0.50 per song

    # Calculate the total number of songs John buys per month
    total_songs_per_month = (music_hours_per_month * music_minutes_per_hour) / song_length_in_minutes

    # Calculate the total cost John pays for music per month
    total_cost_per_month = total_songs_per_month * cost_per_song

    # Calculate the total cost John pays for music per year
    total_cost_per_year = total_cost_per_month * 12

    result = total_cost_per_year
    return result

print(solution())