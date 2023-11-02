def solution():
    # Calculate the number of movies Johnny TV produces in a year
    johnny_movies = 220 * 1.25  # Johnny TV makes 25% more movies than L&J Productions
    total_movies = (220 + johnny_movies) * 5  # Total movies produced in 5 years
    result = total_movies
    return result

print(solution())