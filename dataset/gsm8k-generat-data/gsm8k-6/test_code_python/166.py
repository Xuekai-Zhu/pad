def solution():
    # Calculate the total number of minutes Grandpa watched on Tuesday
    tuesday_minutes = 4 * 60 + 30  # 4 hours and 30 minutes

    # Calculate the total number of movies Grandpa watched on Wednesday
    wednesday_movies = 2 * tuesday_movies

    # Calculate the maximum number of movies Grandpa could have watched during these two days
    max_movies = (tuesday_minutes + wednesday_movies * 90) // 90  # integer division
    result = max_movies
    return result

print(solution())