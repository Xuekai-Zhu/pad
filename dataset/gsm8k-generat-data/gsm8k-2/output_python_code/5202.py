def solution():
    """Lucy is listening to her favorite album while jumping rope. She can jump the rope 1 time per second. If the album's songs are all 3.5 minutes long and there are 10 songs, how many times will she jump rope?"""
    album_length = 3.5 * 60 # convert minutes to seconds
    songs = 10
    jumps_per_song = album_length // songs # integer division to round down
    total_jumps = jumps_per_song * songs
    result = total_jumps
    return result

print(solution())