def solution():
    """Jay went to watch a singer in a one hour 20 minutes concert. If there was a 10-minute intermission, and all the songs were 5 minutes except for one song that lasted 10 minutes, how many songs did she sing?"""
    # Define the total length of the concert in minutes
    concert_length = 80

    # Subtract the length of the intermission
    concert_length -= 10

    # Calculate the number of 5-minute songs
    num_songs = concert_length // 5

    # If there was a 10-minute song, add it to the count
    if concert_length % 5 >= 2.5:
        num_songs += 1

    # Return the result
    result = num_songs
    return result

print(solution())