def solution():
    songs_per_month = 3  # Seal releases 3 songs every month
    money_per_song = 2000  # Seal gets $2000 per song
    months_per_year = 12  # There are 12 months in a year
    years = 3  # Seal wants to know how much money he will get in his first 3 years

    # Calculate the total number of songs Seal will release in 3 years
    total_songs = songs_per_month * months_per_year * years

    # Calculate the total amount of money Seal will get in 3 years
    total_money = total_songs * money_per_song
    result = total_money
    return result

print(solution())