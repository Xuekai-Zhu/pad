def solution():
    
    l_and_j_movies = 220
    johnny_tv_percent_more = 0.25
    johnny_tv_movies = l_and_j_movies * (1 + johnny_tv_percent_more)
    total_movies = (l_and_j_movies + johnny_tv_movies) * 5
    result = total_movies
    return result

print(solution())