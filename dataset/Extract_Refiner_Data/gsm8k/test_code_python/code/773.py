def solution():
    
    # Define the number of movies and the cost of a normal movie
    num_movies = 600
    normal_movie_cost = 10

    # Calculate the number of movies in the series
    series_movies = num_movies // 3

    # Calculate the cost of the series movies
    series_cost = series_movies * 6

    # Calculate the number of remaining movies
    remaining_movies = num_movies - series_movies

    # Calculate the cost of the older movies
    older_movie_cost = remaining_movies * 0.4 * 5

    # Calculate the total cost of replacing the movies
    total_cost = series_cost + older_movie_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())