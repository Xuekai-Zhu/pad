def solution():
    
    # Define the number of songs on Gabriel and Luri
    gabriel_songs = 20
    luri_songs = 3 * gabriel_songs

    # Calculate the number of songs that can be added to Gabriel and Luri
    gabriel_extra_songs = gabriel_songs - luri_songs
    luri_extra_songs = luri_songs - gabriel_extra_songs

    # Calculate the difference between Luri and Gabriel's songs
    difference = luri_extra_songs - gabriel_extra_songs

    # Display the difference
    result = difference
    return result

print(solution())