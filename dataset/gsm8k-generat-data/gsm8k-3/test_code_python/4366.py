def solution():
    """Seal releases 3 songs every month.  He gets $2000 per song.  How much money does he get in his first 3 years?"""
    # Define the number of songs released per month and the price per song
    SONGS_PER_MONTH = 3
    PRICE_PER_SONG = 2000
    MONTHS_PER_YEAR = 12
    YEARS = 3

    # Calculate the total number of songs released in 3 years
    total_songs = SONGS_PER_MONTH * MONTHS_PER_YEAR * YEARS

    # Calculate the total amount of money earned from the songs
    total_earnings = total_songs * PRICE_PER_SONG

    # Display the total earnings
    result = total_earnings
    return result

print(solution())