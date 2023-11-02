def solution():
    # Define the number of days Mark does a gig
    num_days = 14

    # Define the length of the first two songs
    song1_length = 5
    song2_length = 5

    # Define the length of the third song
    song3_length = 2 * song2_length

    # Calculate the total number of minutes Mark played
    total_minutes = num_days * (3 * (song1_length + song2_length) + song3_length)
    result = total_minutes
    return result

print(solution())