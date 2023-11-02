def solution():
    songs_per_month = 3
    payment_per_song = 2000
    months_per_year = 12
    years = 3

    # Calculate the total number of songs he releases in 3 years
    total_songs = songs_per_month * months_per_year * years

    # Calculate the total payment he receives for all the songs released
    total_payment = total_songs * payment_per_song
    result = total_payment
    return result

print(solution())