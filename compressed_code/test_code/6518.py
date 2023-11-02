def solution():
    
    minutes_per_mile = 12
    movies_watched = 2
    movie_length = 1.5 
    total_time = movies_watched * movie_length * 60 
    total_distance = total_time / minutes_per_mile
    result = total_distance
    return result

print(solution())