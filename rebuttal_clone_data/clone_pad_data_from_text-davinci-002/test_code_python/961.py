def solution():
    l_and_j_movies = 220
    johnny_tv_percent_increase = 25
    johnny_tv_increase = l_and_j_movies * (johnny_tv_percent_increase / 100)
    johnny_tv_movies = johnny_tv_increase + l_and_j_movies
    total_movies = l_and_j_movies + johnny_tv_movies
    result = total_movies
    return result

print(solution())