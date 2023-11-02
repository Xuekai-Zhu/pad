def solution():
    
    movie1_length = 90 / 60      
    movie2_length = (90 + 30) / 60      
    total_movie_length = movie1_length + movie2_length
    popcorn_time = 10 / 60      
    fries_time = 2 * popcorn_time
    total_cook_time = popcorn_time + fries_time
    total_time = total_cook_time + total_movie_length
    result = total_time
    return result

print(solution())