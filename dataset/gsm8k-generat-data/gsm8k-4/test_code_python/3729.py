def solution():
    """Stan makes a playlist for the next time he goes running. He has 10 3-minute songs and 15 2-minute songs on his playlist. His entire run takes 100 minutes. If Stan wants a playlist to cover his entire run, how many more minutes of songs will he need in his playlist?"""
    # Define the number and length of songs on Stan's playlist
    num_songs = 10 + 15
    song_lengths = [3] * 10 + [2] * 15

    # Calculate the total length of songs on Stan's playlist
    total_minutes = sum(song_lengths)

    # Calculate the remaining minutes needed for a full run
    remaining_minutes = 100 - total_minutes

    # Return the result
    result = remaining_minutes
    return result

print(solution())