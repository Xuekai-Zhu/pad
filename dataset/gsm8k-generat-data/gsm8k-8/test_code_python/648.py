def solution():
    # Calculate the total number of songs played in the first and second sets
    first_set_songs = 5
    second_set_songs = 7
    total_songs_played = first_set_songs + second_set_songs

    # Calculate the remaining number of songs in the repertoire
    remaining_songs = 30 - total_songs_played - 2

    # Calculate the average number of songs played in the third and fourth sets
    average_songs_per_set = remaining_songs / 2
    result = average_songs_per_set
    return result

print(solution())