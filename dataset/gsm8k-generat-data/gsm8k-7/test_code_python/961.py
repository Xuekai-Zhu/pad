def solution():
    lj_productions = 220
    johnny_tv = lj_productions * 1.25  # Johnny TV makes 25% more movies than L&J Productions

    # Calculate the total number of movies produced by both companies in one year
    total_movies_per_year = lj_productions + johnny_tv

    # Calculate the total number of movies produced by both companies in five years
    total_movies_five_years = total_movies_per_year * 5

    result = total_movies_five_years
    return result

print(solution())