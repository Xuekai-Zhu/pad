def solution():
    lj_movies_per_year = 220  # L&J Productions produces 220 movies per year
    jt_movies_per_year = lj_movies_per_year * 1.25  # Johnny TV makes 25% more movies than L&J Productions
    total_movies_per_year = lj_movies_per_year + jt_movies_per_year  # Total number of movies produced per year

    # Calculate the total number of movies produced in 5 years
    total_movies_five_years = total_movies_per_year * 5

    result = total_movies_five_years
    return result

print(solution())