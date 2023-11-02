def solution():
    
    songs_per_month = 3
    song_price = 2000
    months_per_year = 12
    years = 3
    total_songs = songs_per_month * months_per_year * years
    total_income = total_songs * song_price
    result = total_income
    return result

print(solution())