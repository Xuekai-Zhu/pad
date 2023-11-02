def solution():
    """Beyonce releases 5 different singles on iTunes. Then she releases 2 albums that each has 15 songs and 1 album that has 20 songs. How many songs has Beyonce released in total?"""
    # Define the number of singles and songs in each album
    num_singles = 5
    album1_songs = 15
    album2_songs = 15
    album3_songs = 20

    # Calculate the total number of songs
    total_songs = num_singles + album1_songs + album2_songs + album3_songs

    # return the result
    result = total_songs
    return result

print(solution())