def solution():
    # Define the number of songs downloaded in the morning
    morning_songs = 10

    # Define the number of songs downloaded later on
    later_songs = 15

    # Define the number of songs recommended by her friend
    friend_songs = 3

    # Calculate the total number of new songs downloaded
    total_songs = morning_songs + later_songs + friend_songs

    # Calculate the total memory space required
    total_memory = total_songs * 5

    result = total_memory
    return result

print(solution())