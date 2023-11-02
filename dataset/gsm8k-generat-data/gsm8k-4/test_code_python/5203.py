def solution():
    """Lucy is listening to her favorite album while jumping rope. She can jump the rope 1 time per second. If the album's songs are all 3.5 minutes long and there are 10 songs, how many times will she jump rope?"""
    # Define the length of each song and the total number of songs
    song_length = 3.5
    num_songs = 10

    # Calculate the total length of the album in seconds
    album_length = song_length * 60 * num_songs

    # Calculate the number of jumps Lucy can do during the entire album
    num_jumps = int(album_length)

    # return the result
    result = num_jumps
    return result

print(solution())