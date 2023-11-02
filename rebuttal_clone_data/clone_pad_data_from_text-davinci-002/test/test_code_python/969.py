def solution():
    total_students = 400
    percent_playing_sports = 52
    percent_playing_soccer = 12.5
    students_playing_sports = total_students * (percent_playing_sports / 100)
    soccer_players = students_playing_sports * (percent_playing_soccer / 100)
    result = soccer_players
    
    return result

print(solution())