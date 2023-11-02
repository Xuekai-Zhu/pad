def solution():
    
    tuesday_time = 4 * 60 + 30 
    tuesday_movies = tuesday_time // 90
    wednesday_movies = 2 * tuesday_movies
    total_movies = tuesday_movies + wednesday_movies
    result = total_movies
    return result

print(solution())