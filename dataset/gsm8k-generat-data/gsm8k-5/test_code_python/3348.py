def solution():
    hit_songs = 25
    top_100_songs = hit_songs + 10
    unreleased_songs = hit_songs - 5

    # Total number of songs written by Skyler
    total_songs = hit_songs + top_100_songs + unreleased_songs
    result = total_songs
    return result

print(solution())