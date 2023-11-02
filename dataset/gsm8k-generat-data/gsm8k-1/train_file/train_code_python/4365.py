def solution():
    """Seal releases 3 songs every month. He gets $2000 per song. How much money does he get in his first 3 years?"""
    songs_per_month = 3
    months_per_year = 12
    years = 3
    price_per_song = 2000
    total_songs = songs_per_month * months_per_year * years
    total_money = total_songs * price_per_song
    result = total_money
    return result

print(solution())