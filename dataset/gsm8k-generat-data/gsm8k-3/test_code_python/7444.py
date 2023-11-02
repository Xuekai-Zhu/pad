def solution():
    """Mark does a gig every other day for 2 weeks.  For each gig, he plays 3 songs.  2 of the songs are 5 minutes long and the last song is twice that long.  How many minutes did he play?"""
    # Define the length of the first two songs
    SONG_1_LENGTH = 5
    SONG_2_LENGTH = 5

    # Define the factor by which the third song is longer
    SONG_3_FACTOR = 2

    # Define the number of gigs Mark played
    num_gigs = 7

    # Calculate the length of the third song
    song_3_length = SONG_1_LENGTH * SONG_3_FACTOR

    # Calculate the total length of all the songs for each gig
    gig_length = SONG_1_LENGTH + SONG_2_LENGTH + song_3_length

    # Calculate the total length of all the gigs
    total_length = num_gigs * gig_length

    # Display the total length
    result = total_length
    return result

print(solution())