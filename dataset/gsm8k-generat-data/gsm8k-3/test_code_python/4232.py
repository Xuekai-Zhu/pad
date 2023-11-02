def solution():
    """Beyonce releases 5 different singles on iTunes. Then she releases 2 albums that each has 15 songs and 1 album that has 20 songs. How many songs has Beyonce released in total?"""
    # Define the number of singles and songs per album
    SINGLES = 5
    ALBUM_1 = 15
    ALBUM_2 = 15
    ALBUM_3 = 20

    # Calculate the total number of songs
    total_songs = SINGLES + (ALBUM_1 + ALBUM_2 + ALBUM_3) * 2

    # Display the total number of songs
    result = total_songs
    return result

print(solution())