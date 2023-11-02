def solution():
    """The school band has 30 songs in their repertoire. The band played 5 songs in their first set and 7 in their second set. The band will play 2 songs for their encore. Assuming the band plays through their entire repertoire, how many songs will they play on average in the third and fourth sets?"""
    total_songs = 30
    first_set_songs = 5
    second_set_songs = 7
    encore_songs = 2
    remaining_songs = total_songs - (first_set_songs + second_set_songs + encore_songs)
    third_set_songs = remaining_songs // 2
    fourth_set_songs = remaining_songs - third_set_songs
    total_sets = 4
    average_songs_per_set = (first_set_songs + second_set_songs + third_set_songs + fourth_set_songs + encore_songs) / total_sets
    result = average_songs_per_set
    return result

print(solution())