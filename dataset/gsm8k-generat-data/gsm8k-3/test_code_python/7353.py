def solution():
    """Jay went to watch a singer in a one hour 20 minutes concert.  If there was a 10-minute intermission, and all the songs were 5 minutes except for one song that lasted 10 minutes, how many songs did she sing?"""
    # Calculate the total duration of the concert in minutes
    concert_duration = 80

    # Subtract the duration of the intermission from the total duration of the concert
    concert_duration -= 10

    # Determine how many 5-minute songs were played
    num_5min_songs = (concert_duration // 5) - 1

    # Add the one 10-minute song that was played
    total_num_songs = num_5min_songs + 1

    # Display the total number of songs played
    result = total_num_songs
    return result

print(solution())