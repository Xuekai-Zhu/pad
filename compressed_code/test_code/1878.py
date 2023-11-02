def solution():
    
    vivian_songs = 10
    clara_songs = vivian_songs - 2
    weekdays_in_june = 30 - 8
    vivian_total_songs = vivian_songs * weekdays_in_june
    clara_total_songs = clara_songs * weekdays_in_june
    total_songs = vivian_total_songs + clara_total_songs
    result = total_songs
    return result

print(solution())