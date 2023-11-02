def solution():
    
    tuesday_minutes = 270
    wednesday_minutes = 2 * tuesday_minutes
    total_minutes = tuesday_minutes + wednesday_minutes
    movies_watched = total_minutes / 90
    result = int(movies_watched)
    return result

print(solution())