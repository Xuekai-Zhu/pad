def solution():
    morning_downloads = 10  # Kira downloads 10 songs in the morning
    afternoon_downloads = 15  # Kira downloads 15 more songs in the afternoon
    evening_downloads = 3  # Kira downloads 3 more songs at night
    song_size = 5  # Each song has a size of 5 MB

    # Calculate the total size of the new songs in MB
    total_size = (morning_downloads + afternoon_downloads + evening_downloads) * song_size

    result = total_size
    return result

print(solution())