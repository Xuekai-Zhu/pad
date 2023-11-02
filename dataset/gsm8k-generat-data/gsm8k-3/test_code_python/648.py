def solution():
    """The school band has 30 songs in their repertoire. The band played 5 songs in their first set and 7 in their second set. The band will play 2 songs for their encore. Assuming the band plays through their entire repertoire, how many songs will they play on average in the third and fourth sets?"""
    # Define the number of songs played in the first and second sets, and the encore
    set1_songs = 5
    set2_songs = 7
    encore_songs = 2

    # Calculate the number of songs remaining after the first and second sets, and the encore
    remaining_songs = 30 - (set1_songs + set2_songs + encore_songs)

    # Calculate the average number of songs in the third and fourth sets
    avg_songs = remaining_songs / 2

    # Display the average number of songs
    result = avg_songs
    return result

print(solution())