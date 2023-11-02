def solution():
    """The school band has 30 songs in their repertoire. The band played 5 songs in their first set and 7 in their second set. The band will play 2 songs for their encore. Assuming the band plays through their entire repertoire, how many songs will they play on average in the third and fourth sets?"""
    # Define the total number of songs in the band's repertoire
    total_songs = 30

    # Calculate the number of songs played in the first and second sets
    first_set_songs = 5
    second_set_songs = 7

    # Calculate the number of songs left for the third and fourth sets
    remaining_songs = total_songs - first_set_songs - second_set_songs - 2

    # Divide the remaining songs equally between the third and fourth sets
    third_set_songs = fourth_set_songs = remaining_songs / 2

    # Calculate the average number of songs played in the third and fourth sets
    avg_songs = (third_set_songs + fourth_set_songs) / 2

    result = avg_songs
    return result

print(solution())