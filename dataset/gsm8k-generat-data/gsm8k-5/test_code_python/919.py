def solution():
    initial_songs = 500  # Aisha starts with 500 songs
    added_songs_1 = 500  # Aisha adds another 500 songs the week after
    added_songs_2 = 2 * initial_songs  # Aisha adds twice the initial number of songs
    removed_songs = 50  # Aisha removes 50 songs

    # Calculate the total number of songs on Aisha's mp3 player
    total_songs = initial_songs + added_songs_1 + added_songs_2 - removed_songs
    result = total_songs
    return result

print(solution())