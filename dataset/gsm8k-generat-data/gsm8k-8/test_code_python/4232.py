def solution():
    # Calculate the total number of songs from the 2 albums with 15 songs each
    total_songs = 2 * 15

    # Calculate the total number of songs from the album with 20 songs
    total_songs += 20

    # Add the 5 singles to the total number of songs
    total_songs += 5

    result = total_songs
    return result

print(solution())