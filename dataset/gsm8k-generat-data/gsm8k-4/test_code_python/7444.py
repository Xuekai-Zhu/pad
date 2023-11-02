def solution():
    """Mark does a gig every other day for 2 weeks. For each gig, he plays 3 songs. 2 of the songs are 5 minutes long and the last song is twice that long. How many minutes did he play?"""
    # Define the number of gigs and songs
    num_gigs = 7
    num_songs = 3

    # Define the length of the first two songs
    first_two_song_length = 5

    # Define the length of the last song
    last_song_length = first_two_song_length * 2

    # Calculate the total length of each gig
    gig_length = (2 * first_two_song_length) + last_song_length

    # Calculate the total length of all gigs
    total_length = gig_length * num_gigs

    # Calculate the total length in minutes
    total_length_minutes = total_length * num_songs

    result = total_length_minutes
    return result

print(solution())