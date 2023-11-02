def solution():
    repertoire = 30
    first_set = 5
    second_set = 7
    encore = 2

    # Calculate the total number of songs played in the first two sets and encore
    total_songs_played = first_set + second_set + encore

    # Calculate the number of songs left in the repertoire after the first two sets and encore
    songs_left = repertoire - total_songs_played

    # Divide the remaining songs evenly between the third and fourth sets to find the average number of songs played
    avg_songs_per_set = songs_left / 2
    result = avg_songs_per_set
    return result

print(solution())