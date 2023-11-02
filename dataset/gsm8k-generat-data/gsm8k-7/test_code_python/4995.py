def solution():
    num_hours_per_month = 20
    num_minutes_per_hour = 60
    avg_song_length = 3  # minutes
    cost_per_song = 0.5

    # Calculate the total number of songs John buys in a year
    total_num_songs_per_year = num_hours_per_month * num_minutes_per_hour / avg_song_length * 12

    # Calculate the total cost of all songs John buys in a year
    total_cost_per_year = total_num_songs_per_year * cost_per_song
    result = total_cost_per_year
    return result

print(solution())