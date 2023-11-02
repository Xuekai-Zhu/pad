def solution():
    # Calculate the number of songs Vivian plays in June (30 days - 8 weekend days)
    vivian_songs = 22 * 10  # Vivian plays 10 songs every day except weekends

    # Calculate the number of songs Clara plays in June (30 days - 8 weekend days)
    clara_songs = 22 * 8  # Clara plays 2 fewer songs each day than Vivian, and does not play on weekends
    clara_songs -= 2*8  # Clara does not play on weekends, so subtract 2 songs per day for 8 weekend days

    # Calculate the total number of songs they both listened to in June
    total_songs = vivian_songs + clara_songs
    result = total_songs
    return result

print(solution())