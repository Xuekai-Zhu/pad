def solution():
    time_per_song = 10 * 10  # The singer spends 10 hours a day working on each song
    days_per_song = 10  # Each song takes 10 days to complete
    total_songs = 3  # The singer is releasing 3 songs in one month

    # Calculate the total time the singer took to complete the 3 songs
    total_time = time_per_song * days_per_song * total_songs
    result = total_time
    return result

print(solution())