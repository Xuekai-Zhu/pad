def solution():
    # Calculate the total number of songs played in the first and second sets
    total_songs_played = 5 + 7

    # Calculate the number of songs remaining in the repertoire
    songs_remaining = 30 - total_songs_played - 2  # 2 songs for encore

    # Calculate the average number of songs played in the third and fourth sets
    avg_songs_per_set = songs_remaining / 2

    result = avg_songs_per_set
    return result

print(solution())