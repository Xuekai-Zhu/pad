def solution():
    """Johnny TV makes 25 percent more movies than L&J Productions each year. If  L&J Productions produces 220 movies in a year, how many movies does the two production companies produce in five years combined?"""
    # Calculate the number of movies produced by Johnny TV
    lj_movies = 220
    jt_movies = lj_movies * 1.25

    # Calculate the total number of movies produced in one year
    total_movies = lj_movies + jt_movies

    # Calculate the number of movies produced in five years
    total_movies_five_years = total_movies * 5

    result = total_movies_five_years
    return result

print(solution())