def solution():
    flight_length_hours = 10
    episode_length_minutes = 25
    episodes_watched = 3
    sleep_length_hours = 4.5 
    movie_length_minutes = 105
    movies_watched = 2
    total_activity_length_minutes = episode_length_minutes * episodes_watched + sleep_length_hours * 60 + movie_length_minutes * movies_watched
    result = (flight_length_hours * 60) - total_activity_length_minutes
    
    return result

print(solution())