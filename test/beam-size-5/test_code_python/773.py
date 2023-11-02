def solution():
    
    # Define the number of movies and the cost of a normal movie
    num_movies = 600
    normal_movie_cost = 10

    # Calculate the number of movies in the series
    num_series_movies = num_movies // 3

    # Calculate the cost of the normal movie
    normal_movie_cost = num_movies * normal_movie_cost

    # Calculate the number of remaining movies
    num_remaining_movies = num_movies - num_movies - num_series_movies

    # Calculate the cost of the older movies
    older_movie_cost = num_remaining_movies * 0.4

    # Calculate the total cost of replacing the movies
    total_cost = (num_normal_movies * normal_movie_cost) + (num_older_movies * older_movie_cost)

    # Display the total cost of replacing the movies
    result = total_cost
    return result

print(solution())