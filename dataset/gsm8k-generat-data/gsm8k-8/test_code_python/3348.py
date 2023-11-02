def solution():
    # Define the number of hit songs
    hit_songs = 25

    # Calculate the number of top 100 songs
    top_100_songs = hit_songs + 10

    # Calculate the number of unreleased songs
    unreleased_songs = hit_songs - 5

    # Calculate the total number of songs
    total_songs = hit_songs + top_100_songs + unreleased_songs

    result = total_songs
    return result

print(solution())