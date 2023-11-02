def solution():
    # Calculate the total number of songs written by Skyler
    hit_songs = 25
    top100_songs = hit_songs + 10  # ten more songs than the hit songs
    unreleased_songs = hit_songs - 5  # 5 fewer songs than the hit songs that were never released
    total_songs = hit_songs + top100_songs + unreleased_songs
    result = total_songs
    return result

print(solution())