def solution():
    """Seal releases 3 songs every month. He gets $2000 per song. How much money does he get in his first 3 years?"""
    # Define the number of songs released per month and the price per song
    SONGS_PER_MONTH = 3
    PRICE_PER_SONG = 2000

    # Calculate the total number of songs released in 3 years
    total_songs = SONGS_PER_MONTH * 12 * 3

    # Calculate the total earnings from the songs
    total_earnings = total_songs * PRICE_PER_SONG

    # return the result
    result = total_earnings
    return result

print(solution())