def solution():
    """Johnny TV makes 25 percent more movies than L&J Productions each year. If L&J Productions produces 220 movies in a year, how many movies does the two production companies produce in five years combined?"""
    l_and_j_movies = 220
    johnny_tv_percent_more = 0.25
    johnny_tv_movies = l_and_j_movies * (1 + johnny_tv_percent_more)
    total_movies = (l_and_j_movies + johnny_tv_movies) * 5
    result = total_movies
    return result

print(solution())