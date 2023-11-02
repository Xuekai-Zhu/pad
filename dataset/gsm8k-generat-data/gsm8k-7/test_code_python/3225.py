def solution():
    num_dvd_movies = 8
    dvd_movie_price = 12
    num_bluray_movies = 4
    bluray_movie_price = 18

    # Calculate the total cost of all DVD movies
    total_dvd_cost = num_dvd_movies * dvd_movie_price

    # Calculate the total cost of all Blu-ray movies
    total_bluray_cost = num_bluray_movies * bluray_movie_price

    # Calculate the total number of movies
    total_num_movies = num_dvd_movies + num_bluray_movies

    # Calculate the average price per movie
    avg_price_per_movie = (total_dvd_cost + total_bluray_cost) / total_num_movies
    result = avg_price_per_movie
    return result

print(solution())