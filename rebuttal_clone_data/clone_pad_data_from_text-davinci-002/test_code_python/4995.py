def solution():
    hours_per_month = 20
    minutes_per_song = 3
    months_per_year = 12
    price_per_song = .50
    total_songs = hours_per_month * minutes_per_song * months_per_year
    total_cost = total_songs * price_per_song
    result = total_cost
    
    return result

print(solution())