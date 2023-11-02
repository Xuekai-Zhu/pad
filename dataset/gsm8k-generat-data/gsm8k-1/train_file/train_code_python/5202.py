def solution():
    """Lucy is listening to her favorite album while jumping rope. She can jump the rope 1 time per second. If the album's songs are all 3.5 minutes long and there are 10 songs, how many times will she jump rope?"""
    seconds_per_song = 3.5 * 60
    jumps_per_song = 1 * seconds_per_song
    total_jumps = jumps_per_song * 10
    result = total_jumps
    return result

print(solution())