def solution():
    songs_weekdays = 10
    songs_weekends = 0
    days_in_month = 30
    weekends_in_month = 8
    total_days = days_in_month - weekends_in_month
    total_songs = (songs_weekdays * total_days) + (songs_weekends * weekends_in_month)
    result = total_songs
    return result

print(solution())