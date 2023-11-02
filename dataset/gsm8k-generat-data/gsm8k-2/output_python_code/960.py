def solution():
    """Johnny TV makes 25 percent more movies than L&J Productions each year. If L&J Productions produces 220 movies in a year, how many movies does the two production companies produce in five years combined?"""
    lj_productions = 220
    johnny_tv = lj_productions * 1.25
    total_movies = (lj_productions + johnny_tv) * 5
    result = total_movies
    return result

print(solution())