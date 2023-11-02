def solution():
    # Calculate the number of movies produced by Johnny TV in a year
    johnny_movies = 1.25 * 220

    # Calculate the total number of movies produced by both companies in one year
    total_movies = johnny_movies + 220

    # Calculate the total number of movies produced by both companies in five years
    total_movies_5_years = 5 * total_movies

    result = total_movies_5_years
    return result

print(solution())