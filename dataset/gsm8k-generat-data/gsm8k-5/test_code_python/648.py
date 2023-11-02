def solution():
    repertoire = 30  # The band has 30 songs in their repertoire
    first_set = 5  # The band played 5 songs in their first set
    second_set = 7  # The band played 7 songs in their second set
    encore = 2  # The band will play 2 songs for their encore

    # Calculate the number of songs played in the first two sets and the encore
    total_songs = first_set + second_set + encore

    # Calculate the number of songs left to play
    remaining_songs = repertoire - total_songs

    # Calculate the average number of songs played in the third and fourth sets
    avg_songs = remaining_songs / 2
    result = avg_songs
    return result

print(solution())